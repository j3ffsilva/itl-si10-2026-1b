#!/usr/bin/env python3
import csv
import json
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent
LISTING = BASE_DIR / "listagem-das-entregas.tsv"
OUT_DIR = BASE_DIR / "entregas"


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value or "sem-nome"


def drive_file_id(url: str) -> Optional[str]:
    patterns = [
        r"/drive/([A-Za-z0-9_-]+)",
        r"/file/d/([A-Za-z0-9_-]+)",
        r"[?&]id=([A-Za-z0-9_-]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def github_repo(url: str):
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc.lower() != "github.com":
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return None
    return parts[0], parts[1].removesuffix(".git")


def urlopen_with_headers(url: str) -> urllib.response.addinfourl:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 entrega-downloader/1.0",
        },
    )
    return urllib.request.urlopen(request, timeout=60)


def download_url(url: str, target: Path) -> tuple[bool, str]:
    try:
        with urlopen_with_headers(url) as response:
            content = response.read()
            target.write_bytes(content)
            content_type = response.headers.get("Content-Type", "")
        return True, f"{len(content)} bytes; {content_type}"
    except Exception as exc:
        return False, str(exc)


def download_drive_file(file_id: str, target: Path) -> tuple[bool, str]:
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    ok, detail = download_url(url, target)
    if not ok:
        return ok, detail
    content = target.read_bytes()
    head = content[:1024].lstrip().lower()
    if head.startswith(b"<html") or head.startswith(b"<!doctype html"):
        return False, "download produced an HTML page instead of the file"
    try:
        notebook = json.loads(content.decode("utf-8"))
    except Exception:
        return False, "downloaded content is not a valid UTF-8 JSON notebook"
    if notebook.get("nbformat") is None:
        return False, "downloaded JSON is missing notebook nbformat"
    return True, detail


def clone_github(url: str, target: Path) -> tuple[bool, str]:
    if target.exists():
        return True, "repository directory already exists"
    result = subprocess.run(
        ["git", "clone", "--depth", "1", url, str(target)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=180,
    )
    return result.returncode == 0, result.stdout.strip()


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(exist_ok=True)
    rows = list(csv.DictReader(LISTING.open(encoding="utf-8-sig"), delimiter="\t"))
    summary = []

    for index, row in enumerate(rows, start=1):
        name = row["Nome do estudante"].strip()
        url = row["Link da atividade"].strip()
        student_dir = OUT_DIR / f"{index:02d}-{slugify(name)}"
        student_dir.mkdir(parents=True, exist_ok=True)

        metadata = {
            "student": name,
            "url": url,
            "kind": "unknown",
            "status": "pending",
            "files": [],
            "notes": [],
        }
        stale_source_url = student_dir / "source_url.txt"

        repo = github_repo(url)
        file_id = drive_file_id(url)

        if repo:
            metadata["kind"] = "github"
            repo_dir = student_dir / "repo"
            ok, detail = clone_github(url, repo_dir)
            metadata["status"] = "downloaded" if ok else "failed"
            metadata["files"] = [str(repo_dir.relative_to(student_dir))] if ok else []
            metadata["notes"].append(detail)
        elif file_id:
            metadata["kind"] = "drive_or_colab"
            target = student_dir / f"{file_id}.ipynb"
            ok, detail = download_drive_file(file_id, target)
            if ok:
                if stale_source_url.exists():
                    stale_source_url.unlink()
                metadata["status"] = "downloaded"
                metadata["files"] = [target.name]
            else:
                fallback = student_dir / "source_url.txt"
                fallback.write_text(url + "\n", encoding="utf-8")
                if target.exists():
                    target.unlink()
                metadata["status"] = "failed"
                metadata["files"] = [fallback.name]
                metadata["notes"].append(detail)
        else:
            fallback = student_dir / "source_url.txt"
            fallback.write_text(url + "\n", encoding="utf-8")
            metadata["status"] = "failed"
            metadata["files"] = [fallback.name]
            metadata["notes"].append("could not identify GitHub repository or Drive file id")

        write_json(student_dir / "metadata.json", metadata)
        summary.append(
            {
                "student": name,
                "kind": metadata["kind"],
                "status": metadata["status"],
                "path": str(student_dir.relative_to(BASE_DIR)),
            }
        )
        print(f"{index:02d} {metadata['status']:10} {metadata['kind']:14} {name}")

    write_json(OUT_DIR / "summary.json", {"submissions": summary})
    failures = [item for item in summary if item["status"] != "downloaded"]
    print(f"\nDownloaded: {len(summary) - len(failures)}/{len(summary)}")
    if failures:
        print("Failures:")
        for item in failures:
            print(f"- {item['student']} ({item['path']})")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
