from django.urls import path
from .views import *

urlpatterns = [
  path('test/', async_test, name='test'),
  path('download_genome/', DownloadGenomeView, name='download_genome'),
  path('scan_raw_data/', ScanRawDataView, name='scan_raw_data'),
  path('refresh_raw_data/', RefreshRawDataView, name='refresh_raw_data'),
]