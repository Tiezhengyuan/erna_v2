from celery import shared_task
from time import sleep
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


@shared_task
def minus(x,y):
  sleep(5)
  return x*y

@shared_task
def sample_task():
    logger.info("The sample task just ran.")