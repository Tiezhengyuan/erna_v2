from django.http import HttpResponse, JsonResponse

from .tasks import *

def download_genome(request):
  data_source = request.GET.get('data_source', '')
  specie = request.GET.get('specie')
  dna_task_id = download_genome_dna.delay(
    data_source, specie
  )
  annot_task_id = download_genome_annot.delay(
    data_source, specie
  )
  res = {
    'download_genome_dna': str(dna_task_id),
    'download_genome_annot': str(annot_task_id),
  }
  return JsonResponse(res, safe=False)

def scan_raw_data(request):
  dir_raw_data = request.GET.get('dir_raw_data', '')
  task_id = download_genome_dna.delay(dir_raw_data)
  res = {
    'scan_raw_data': str(task_id),
  }
  return JsonResponse(res, safe=False)



def async_test(request):
  task_id = minus.delay(2, 3)
  return HttpResponse(task_id)