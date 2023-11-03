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

  def create(self, request):
      project_id = request.data.get('project_id')
      if project_id is not None:
        res = Task.objects.add_new_task(request.data)
        return Response(res)
      return Response({'error': 'project_id is missing.'})
  
  @action(detail=False, methods=['get'])
  def list_tasks(self, request):
    serialized_data = serializers.serialize('json', self.get_queryset())
    serialized_data = json.loads(serialized_data)
    res = []
    for item in serialized_data:
      fields = item['fields']
      fields['params'] = json.loads(fields['params'])
      res.append(fields)
    return Response(res)
  
