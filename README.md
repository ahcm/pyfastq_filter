# pyfastq_filter

Filter FASTQ Files.

# Installation

```bash
pip3 install --user pyfastq_filter
```

# Usage

```
Usage:
  pyfastq_filter.py [-q i] [-l n] [-o OUTNAME] FASTQ

Options:
  -l --length=n      minimum length to let through [default: 300]
  -q --quality=i     minimum quality to let through [default: 10]
  -o --outfile=FILE  output filename, otherwise STDOUT [default: -]
```


Extract only FASTQ entries with sequence length >= 5000 and mean quality >= 12:

```bash
pyfastq_filter.py -q 12 -l 5000 example.fastq > example-q12-l5000.fastq
```
