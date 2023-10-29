from Bio import SeqIO
from pipelines.sequence.trim_seq import TrimSeq
from pipelines.biofile.fastq import FASTQ

class TrimAdapter:
  def __init__(self, params:dict):
    self.params = params
  
  def trim_3end_adapter(self):
    trimmer = TrimSeq(
      self.params['adapter'],
      self.params['min_match'],
      '3end',
      self.params['max_err']
    )
    # read fastq
    outfile = self.params['trim']['R1']
    with open(outfile, 'w') as out_handle:
      infile = self.params['fastq']['R1']
      fastq_iter = FASTQ(infile).parse_records()
      for rec in fastq_iter:
        print(rec.id, rec.seq)
        rec.seq = trimmer.trim_3end(rec.seq)
    