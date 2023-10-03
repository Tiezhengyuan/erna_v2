from django.urls import path
from . import views

urlpatterns = [
  path('test/', views.async_test, name='test'),
  path('download_genome/', views.download_genome, name='download_genome'),
  path('scan_raw_data/', views.scan_raw_data, name='scan_raw_data'),
]