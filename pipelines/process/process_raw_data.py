'''
process raw data namely fastq
'''
import os
from typing import Iterable
from sample.models import RawData
from django.core import serializers
DEFAULT_RAW_DATA_DIR = os.path.join(
  os.path.dirname(os.path.dirname(__file__)), 'raw_data')

class ProcessRawData:
  def __init__(self):
    self.dir_raw_data = os.environ.get(\
      'RAW_DATA_DIR', DEFAULT_RAW_DATA_DIR)

  def scan_raw_data(self):
    raw_data = {'UN': []}
    for batch in os.listdir(self.dir_raw_data):
      path = os.path.join(self.dir_raw_data, batch)
      if os.path.isdir(path):
        raw_data[batch] = []
        for root, dirs, files in os.walk(path, topdown=False):
          for file in files:
            raw_data[batch].append((root, file))
      else:
        raw_data['UN'].append((self.dir_raw_data, batch))
    return raw_data
  
  def refresh_raw_data(self):
    '''
    refresh table RawDATA
    '''
    RawData.objects.all().delete()
    raw_data = self.scan_raw_data()
    data = RawData.objects.load_data(raw_data)
    return serializers.serialize('json', data)
