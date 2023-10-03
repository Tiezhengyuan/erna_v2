from django.http import HttpResponse, JsonResponse

from .tasks import *

def download_genome(request):
  data_source = request.GET.get('data_source', '')
  specie = request.GET.get('specie')
  task_id = download_genome_dna.delay(
    data_source, specie
  )
  res = {
    'download_genome_dna': str(task_id),
  }
  return JsonResponse(res, safe=False)


def async_test(request):
  task_id = minus.delay(2, 3)
  return HttpResponse(task_id)