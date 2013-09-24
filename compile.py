#!/usr/bin/env python

import subprocess, sys, os

exts = ["aux","bbl","blg","log","toc","out"]
files = os.listdir('.')
for fname in files:
    if any(ext in fname for ext in exts):
        os.remove(fname)

subprocess.call(["pdflatex", "thesis.tex"])
subprocess.call(["bibtex", "thesis"])
subprocess.call(["pdflatex", "thesis.tex"])
subprocess.call(["pdflatex", "thesis.tex"])
print "Compiled thesis.tex with full compile."


