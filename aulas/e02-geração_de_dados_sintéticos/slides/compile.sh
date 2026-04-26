#!/bin/bash

name="${1%.tex}"

mkdir -p out
lualatex -output-directory=out "$name.tex" && lualatex -output-directory=out "$name.tex"
mv "out/$name.pdf" .
mv "out/$name.log" .
rm -rf out/