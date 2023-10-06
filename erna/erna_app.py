'''
entrance into pipelines
'''
import os
import sys

import django
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erna.settings')
django.setup()

from pipelines.process import *

def main(args):
  if len(args) < 1:
    print("method should be defined.")
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
      return ProcessRawData().scan_raw_data()
    case 'refresh_raw_data':
      return ProcessRawData().refresh_raw_data()
    case 'genome_alignment':
      if len(args)>=2:
        p = Alignment(args[1])
        return p.genome_alignment()
    case 'genome_assembly':
      if len(args)>=2:
        p = Assembly(args[1])
        return p.genome_aseembly()
    case 'count_reads':
      if len(args)>=3:
        p = Collect(args[1])
        return p.count_reads()

if __name__ == '__main__':
  args = sys.argv[1:]
  main(args)
