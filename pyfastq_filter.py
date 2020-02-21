#!/bin/env python3
# MIT License see LICENSE
# -- Andy Hauser <Andreas.Hauser@LMU.de>
"""
Usage:
  pyfastq_filter.py [-q i] [-l n] [-o OUTNAME] FASTQ

Options:
  -l --length=n      minimum length to let through [default: 300]
  -q --quality=i     minimum quality to let through [default: 10]
  -o --outfile=FILE  output filename, otherwise STDOUT [default: -]
"""
from docopt import docopt

import pyfastq_reader
#import gzip
import sys
import numpy as np

def main():
  arguments = docopt(__doc__)

  length  = int(arguments["--length"])
  quality = int(arguments["--quality"])

  handle = sys.stdin if arguments["FASTQ"] == "-" else open(arguments["FASTQ"])
  output = sys.stdout if arguments["--outfile"] == "-" else open(arguments["--outfile"])

  for head, seq, qual in pyfastq_reader.fastq_reader_fh(handle):
    mean_qual = round(np.mean(bytearray(qual, "ascii")) - 33, 2)
    if len(seq) >= length and mean_qual >= quality:
      print(head, seq, "+", qual, sep="\n", file=output)

if __name__ == '__main__':
  main()
