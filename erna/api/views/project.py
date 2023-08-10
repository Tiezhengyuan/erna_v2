from django.shortcuts import render
from rest_framework import viewsets, response, \
    permissions, decorators

from rna_seq.models import Project
from api.serializers.project import *

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated,]

class ProjectManagerViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectUserSerializer
    permission_classes = [permissions.IsAuthenticated,]