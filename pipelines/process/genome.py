'''
process genome annotations before analysis
'''
from .connector.connect_ncbi import ConnectNCBI
from process.utils.handle_json import HandleJson

class Genome:

  def __init__(self, data_source=None, specie=None, version=None):
    self.data_source = data_source
    self.specie = specie
    self.version = version

  def retrieve_assembly_summary(self):
    res = {}
    if self.data_source == "NCBI":
      # download assembly_summary.txt
      client = ConnectNCBI()
      text_files = client.download_assembly_summary()
      for text_file in text_files.values():
        HandleJson(text_file).from_text()
      #load samples into db.Specie
      res['specie'] = client.load_species()
      #load samples into db.Genome
      res['genome'] = client.load_genomes()
    return res

  def download_genome(self):
    '''
    genome DNA sequences
    '''
    res = {}
    if self.data_source == "NCBI":
      ConnectNCBI().download_genome(self.specie, self.version)
    return res


  def download_annot(self):
    '''
    genome annotations
    '''
    pass







