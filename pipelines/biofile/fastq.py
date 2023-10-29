'''
'''
from Bio import SeqIO
from typing import Iterable


class FASQ:
  def __init__(self, infile:str):
    self.infile = infile
  
  def parse_records(self)->Iterable:
    if self.infile.endswith('.gz'):
      with open(self.infile, 'rt') as f:
        for rec in SeqIO.parse(f, 'fastq'):
          yield rec
    else:
      with open(self.infile, 'r') as f:
        for rec in SeqIO.parse(f, 'fastq'):
          yield rec

