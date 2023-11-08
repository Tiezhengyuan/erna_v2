import json
from django.shortcuts import render
from django.core import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from rna_seq.models import Task
from api.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    config = {}
    for name in ['project_id', 'task_id']:
      val = self.request.query_params.get(name)
      if val is not None:
        config[name] = val
    if config:
      return Task.objects.filter(**config)
    return Task.objects.all()

  @action(detail=False, methods=['post'])
  def load_tasks(self, request):
      project_id = request.data.get('project_id')
      if project_id is not None:
        res = Task.objects.load_tasks(project_id, request.data)
        return Response(res)
      return Response({'error': 'project_id is missing.'})
  
  @action(detail=False, methods=['delete'])
  def delete_tasks(self, request):
    project_id = request.GET.get('project_id')
    task_id = request.GET.get('task_id')
    res = Task.objects.delete_tasks(project_id, task_id)
    return Response(res)
  
