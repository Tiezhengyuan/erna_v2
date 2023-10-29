'''
trim adapter for miRNA-seq
'''
from Bio import SeqIO,SeqRecord, Seq


from pipelines.sequence.trim_seq import TrimSeq
from pipelines.biofile.fastq import FASTQ

class TrimAdapter:
  def __init__(self, params:dict):
    self.params = params

  def __call__(self):
    if self.params['trim_end'] == '3end':
      return self.trim_3end_adapter()
    else:
      print('skipp adapter trimming.')

  def trim_3end_adapter(self):
    info = {
      'total_reads': 0,
      'trimmed_reads': 0,
    }
    trimmer = TrimSeq(
      self.params['adapter'],
      self.params['min_match'],
      '3end',
      self.params['max_err']
    )
    # read fastq
    with open(self.params['output'], 'w') as out_handle:
      fq_iter = FASTQ(self.params['input']).parse_records()
      for rec in fq_iter:
        info['total_reads'] += 1
        trimmed_seq, pos = trimmer.trim_3end(rec.seq)
        if pos > -1:
          rec = rec[:pos]
          info['trimmed_reads'] += 1
        SeqIO.write(rec, out_handle, 'fastq')
    info['trim_percentage'] = round(info['trimmed_reads']\
      /info['total_reads'], 4)
    return info
    