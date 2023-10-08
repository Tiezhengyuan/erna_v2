from django.http import HttpResponse, JsonResponse

from .tasks import *

def DownloadGenomeView(request):
  data_source = request.GET.get('data_source', '')
  specie = request.GET.get('specie')
  dna_task_id = download_genome_dna.delay(
    data_source, specie
  )
  annot_task_id = download_genome_annot.delay(
    data_source, specie
  )
  res = {
    'task_id': [str(dna_task_id), str(annot_task_id)],
  }
  return JsonResponse(res, safe=False)

def ScanRawDataView(request):
  task_id = scan_raw_data.delay()
  res = {
    'task_id': [str(task_id),],
  }
  return JsonResponse(res, safe=False)

def RefreshRawDataView(request):
  task_id = refresh_raw_data.delay()
  res = {
    'task_id': [str(task_id),],
  }
  return JsonResponse(res, safe=False)

def ParseSampleDataView(request):
  study_name = request.GET.get('study_name', '')
  prefix = request.GET.get('prefix')
  postfix = request.GET.get('postfix')
  task_id = parse_sample_data.delay(study_name, prefix, postfix)
  res = {
    'task_id': [str(task_id),],
  }
  return JsonResponse(res, safe=False)

def ResetSampleView(request):
  task_id = reset_sample.delay()
  res = {
    'task_id': [str(task_id),],
  }
  return JsonResponse(res, safe=False)


def async_test(request):
  task_id = minus.delay(2, 3)
  return HttpResponse(task_id)