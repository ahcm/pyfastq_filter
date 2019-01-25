# pyfastq_filter

Filter FASTQ Files.

# Installation

```bash
pip3 install --user pyfastq_filter
```

# Usage

Extract only FASTQ entries with sequence length > 5000:

```bash
pyfastq_filter.py -l 5000 example.fastq > example-l5000.fastq
```
