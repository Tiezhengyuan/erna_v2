from django.urls import path
from . import views

urlpatterns = [
  path('test/', views.async_test, name='test'),
  path('download_genome/', views.download_genome, name='download_genome'),
]