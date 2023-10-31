
class Align:
  def __init__(self, info):
    self.info = info
  
  def collect_annot(self, data_source:str, specie:str, version:str):
    '''
    update db.Annotation based on db.Genome
    '''
    pass

  def build_index(self, aligner:str):
    '''
    build index for genome alignment
    '''
    pass


  def genome_alignment(self):
    pass