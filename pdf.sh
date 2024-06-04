#!/bin/bash

pandoc --top-level-division=chapter \
       -s Rapport.md \
       -o Rapport.pdf \
       -N \
       --toc \
       --filter pandoc-crossref \
       --pdf-engine=xelatex \
       -V documentclass=report
