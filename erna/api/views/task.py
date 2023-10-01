from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from rna_seq.models import Task
from api.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        project_id = request.data.get('project_id')
        if project_id is not None:
          res = Task.objects.add_new_task(request.data)
          return Response(res)
        return Response({'error': 'project_id is missing.'})