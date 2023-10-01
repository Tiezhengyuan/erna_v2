from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from rna_seq.models import Project
from api.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
  serializer_class = ProjectSerializer
  permission_classes = [permissions.IsAuthenticated,]

  def get_queryset(self):
    config = {}
    items = ['owner_id', 'sequencing', 'status', 'project_name']
    for name in items:
      val = self.request.query_params.get(name)
      if val:
        config[name] = val
    if config:
      return Project.objects.filter(**config)
    return Project.objects.all()

  def create(self, request):
    '''
    project_id and owner is automatically generated.
    example: 
    {
      "project_name": "test",
      "description": "for testing",
      "status": "A",
      "sequencing": "M"
    }
    '''
    data = request.data
    data['owner_id'] = request.user.id
    res = Project.objects.insert(data)
    return Response({'project_id': res})

  @action(detail=False, methods=['GET'])
  def next_project_id(self, request):
    res = Project.objects.get_next_project_id()
    return Response({'project_id': res})

  @action(detail=False, methods=['GET'])
  def count(self, request):
    res = Project.objects.all()
    count = res.count()
    return Response({'count': count})

  @action(detail=False, methods=['GET'])
  def owner_projects(self, request):
    res = Project.objects.get_projects_by_owner(request.user)
    return Response(res)
  
  @action(detail=False, methods=['delete'])
  def delete_all(self, request):
    res = Project.objects.all()
    count = res.count()
    res.delete()
    return Response({'message': f"{count} are deleted."})