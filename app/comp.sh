#!/bin/bash

python3 main.py
lilypond-book --output=out --pdf prod/song.tex
pdflatex out/song.tex
mv out/song.pdf .
rm -r out
