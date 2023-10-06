from time import sleep
import subprocess
from django.conf import settings
import sys
sys.path.insert(0, getattr(settings, 'PIPELINES_DIR'))
from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

from process.process_raw_data import ProcessRawData

@shared_task
def download_genome_dna(data_source, specie):
  cmd = ["python", getattr(settings, 'PIPELINE_ERNA'),
    'genome_download_dna', data_source, specie]
  res= subprocess.run(cmd, capture_output=True, text=True)
  return res.stdout, res.stderr

@shared_task
def download_genome_annot(data_source, specie):
  cmd = ["python", getattr(settings, 'PIPELINE_ERNA'),
    'genome_download_annot', data_source, specie]
  res= subprocess.run(cmd, capture_output=True, text=True)
  return res.stdout, res.stderr

@shared_task
def scan_raw_data():
  res = ProcessRawData().scan_raw_data()
  return res

@shared_task
def refresh_raw_data():
  res = ProcessRawData().refresh_raw_data()
  return res

@shared_task
def minus(x,y):
  print(x,y)
  return x*y
