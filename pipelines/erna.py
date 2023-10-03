'''
entrance into pipelines
'''
import os
import sys

from .process import *

def main(args):
  if len(args) < 2:
    print("At least 2 parameters shall be passed into.")
    sys.exit(1)

  match args[0]:
    case 'genome_download_dna':
      if len(args)>=3:
        data_source, specie = args[1], args[2]
        p = Genome(data_source, specie)
        return p.download_dna()
    case 'genome_download_annot':
      if len(args)>=3:
        data_source, specie = args[1], args[2]
        p = Genome(data_source, specie)
        return p.download_annot()
    case 'scan_raw_data':
      p = RawData(args[1])
      return p.scan_raw_data()
    case 'genome_alignment':
      p = Alignment(args[1])
      return p.genome_alignment()
    case 'genome_assembly':
      p = Assembly(args[1])
      return p.genome_aseembly()
    case 'count_reads':
      p = Collect(args[1])
      return p.count_reads()

if __name__ == '__main__':
  args = sys.argv[1:]
  main(args)
