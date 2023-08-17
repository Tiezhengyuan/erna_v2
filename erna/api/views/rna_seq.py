from django.shortcuts import render
from rest_framework import viewsets, response, \
    permissions, decorators

from rna_seq.models import Project, ProjectUser, \
    Task, TaskTree, TaskExecution
from api.serializers import ProjectSerializer, ProjectUserSerializer, \
    TaskSerializer, TaskTreeSerializer, TaskExecutionSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated,]

class ProjectUserViewSet(viewsets.ModelViewSet):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer
    permission_classes = [permissions.IsAuthenticated,]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskTreeViewSet(viewsets.ModelViewSet):
    queryset = TaskTree.objects.all()
    serializer_class = TaskTreeSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskExecutionViewSet(viewsets.ModelViewSet):
    queryset = TaskExecution.objects.all()
    serializer_class = TaskExecutionSerializer
    permission_classes = [permissions.IsAuthenticated]

