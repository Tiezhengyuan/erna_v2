from time import sleep
import subprocess
from django.conf import settings
import sys
sys.path.insert(0, getattr(settings, 'PIPELINES_DIR'))
from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


@shared_task
def download_genome(data_source, specie, version):
  from process.process_genome import ProcessGenome
  p = ProcessGenome(data_source, specie, version)
  return p.download_genome()

@shared_task
def scan_raw_data():
  from process.process_raw_data import ProcessRawData
  return ProcessRawData().scan_raw_data()

@shared_task
def refresh_raw_data():
  from process.process_raw_data import ProcessRawData
  return ProcessRawData().refresh_raw_data()

@shared_task
def parse_sample_data(study_name, prefix=None, postfix=None):
  from process.process_raw_data import ProcessRawData
  c = ProcessRawData()
  return c.parse_sample_data(study_name, prefix, postfix)

@shared_task
def reset_sample():
  from process.process_raw_data import ProcessRawData
  return ProcessRawData().reset_sample()

@shared_task
def trim_adapter(params):
  from process.trim_adapter import TrimAdapter
  return TrimAdapter(params)()

@shared_task
def build_index(data_source, specie, version, aligner):
  from process.align import Align
  c = Align(aligner)
  return c.build_index(data_source, specie, version)


@shared_task
def minus(x,y):
  print(x,y)
  return x*y
