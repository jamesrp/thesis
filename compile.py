#!/usr/bin/env python

import subprocess, sys, os

exts = ["aux","bbl","blg","log","toc","out"]
files = os.listdir('.')
for fname in files:
    if any(ext in fname for ext in exts):
        os.remove(fname)

if len(sys.argv) > 1: # heh
    subprocess.call(["pdflatex", "thesis.tex"])
    subprocess.call(["bibtex", "thesis"])
    subprocess.call(["pdflatex", "thesis.tex"])
    subprocess.call(["pdflatex", "thesis.tex"])
    print "Compiled thesis.tex with full compile."
else:
    # Assume stub
    subprocess.call(["pdflatex", "stub.tex"])
    print "Compiled stub.tex."


