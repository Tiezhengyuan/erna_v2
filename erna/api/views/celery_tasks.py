from django.shortcuts import render
from rest_framework import viewsets, response, \
    permissions, decorators

from django_celery_results.models import TaskResult
from api.serializers import TaskResultSerializer

class TaskResultViewSet(viewsets.ModelViewSet):
  queryset = TaskResult.objects.all()
  serializer_class = TaskResultSerializer