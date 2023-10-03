from time import sleep
import subprocess
from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@shared_task
def download_genome_dna(data_source, specie):
    cmd = ["python", getattr(settings, 'PIPELINE_ERNA'),
      'genome_download_dna', data_source, specie]
    res= subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout

@shared_task
def download_genome_annot(data_source, specie):
    cmd = ["python", getattr(settings, 'PIPELINE_ERNA'),
      'genome_download_annot', data_source, specie]
    res= subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout

@shared_task
def scan_raw_data(data_source, specie):
    cmd = ["python", getattr(settings, 'PIPELINE_ERNA'),
      'scan_raw_data', data_source, specie]
    res= subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout


@shared_task
def minus(x,y):
  print(x,y)
  return x*y
