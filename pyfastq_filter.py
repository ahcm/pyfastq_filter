#!/bin/env python3
# MIT License see LICENSE
# -- Andy Hauser <Andreas.Hauser@LMU.de>
"""
Usage:
  fastq_filter.py [-l n] [-o OUTNAME] FASTQ

Options:
  -l --length=n     minimum length to let through [default: 300]
  -o --outfile=FILE     output filename, otherwise STDOUT [default: -]
"""
from docopt import docopt

from Bio import SeqIO
import pyfastq_reader
import gzip
import sys

def main():
  arguments = docopt(__doc__)
  #print(arguments)

  n = int(arguments["--length"])

  #handle = gzip.open(fasta_file, "rt")
  handle = sys.stdin if arguments["FASTQ"] == "-" else open(arguments["FASTQ"])
  output = sys.stdout if arguments["--outfile"] == "-" else open(arguments["--outfile"])

  for head, seq, qual in pyfastq_reader.fastq_reader_fh(handle):
    if len(seq) >= n:
      print(head, seq, "+", qual, sep="\n")

if __name__ == '__main__':
  main()
