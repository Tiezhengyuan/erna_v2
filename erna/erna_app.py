'''
entrance into pipelines
'''
import os
import sys
DIR_PROJECT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_PROJECT)

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erna.settings')
django.setup()


def main(args):
  if len(args) < 1:
    print("method should be defined.")
    sys.exit(1)

  match args[0]:
    case 'scan_raw_data':
      from pipelines.process import ProcessRawData
      return ProcessRawData().scan_raw_data()
    case 'refresh_raw_data':
      from pipelines.process import ProcessRawData
      return ProcessRawData().refresh_raw_data()
    case 'assembly_summary':
      if len(args) >= 2:
        from pipelines.process import ProcessGenome
        return ProcessGenome(args[1]).retrieve_assembly_summary()
    case 'download_genome':
      '''
      example:

      '''
      if len(args)>=4:
        from pipelines.process import ProcessGenome
        data_source, specie, version = args[1:]
        p = ProcessGenome(data_source, specie, version)
        return p.download_genome()
    case 'trim_adapter':
      '''
      example: 
        python3 erna_app.py trim_adapter ATGGCG \
          /home/yuan/bio/erna_v2/pipelines/tests/data/reads_1.fq \
          /home/yuan/bio/erna_v2/pipelines/tests/temp/reads_1_trimmed.fq
      '''
      if len(args) >=4:
        from pipelines.process.trim_adapter import TrimAdapter
        params =  dict([(k,v) for k, v in zip(['adapter', 'input',\
          'output',], args[1:])])
        return TrimAdapter(params)()



    case 'genome_download_annot':
      if len(args)>=3:
        from pipelines.process import Genome
        data_source, specie = args[1], args[2]
        p = Genome(data_source, specie)
        return p.download_annot()
    
    case 'genome_alignment':
      if len(args)>=2:
        from pipelines.process import Alignment
        p = Alignment(args[1])
        return p.genome_alignment()
    
    case 'genome_assembly':
      if len(args)>=2:
        from pipelines.process import Assembly
        p = Assembly(args[1])
        return p.genome_aseembly()
    case 'count_reads':
      if len(args)>=3:
        from pipelines.process import Collect
        p = Collect(args[1])
        return p.count_reads()
  print('wrong arguments')

if __name__ == '__main__':
  args = sys.argv[1:]
  main(args)
