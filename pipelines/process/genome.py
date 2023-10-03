'''
process genome annotations before analysis
'''

class Genome:
  def __init__(self, data_source, specie):
    self.data_source = data_source
    self.specie = specie
  
  def download_dna(self):
    '''
    genome DNA sequences in fa
    '''
    pass

  def download_annot(self):
    '''
    genome annotations
    '''
    pass