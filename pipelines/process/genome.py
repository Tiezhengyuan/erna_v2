'''
process genome annotations before analysis
'''
from .connector.connect_ncbi import ConnectNCBI
from process.utils.handle_json import HandleJson

class Genome:

  def __init__(self, data_source=None, specie=None):
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

  def retrieve_assembly_summary(self):
    if self.data_source == "NCBI":
      # download assembly_summary.txt
      client = ConnectNCBI()
      text_files = client.download_assembly_summary()
      for text_file in text_files.values():
        HandleJson(text_file).from_text()
      #load samples into db.Specie
      return client.load_species()

  




