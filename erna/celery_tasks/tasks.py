from celery import shared_task
from time import sleep
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@shared_task
def download_genome_dna(data_source, specie):
    return f"{data_source}/{specie}"

@shared_task
def minus(x,y):
  print(x,y)
  return x*y
