from django.shortcuts import render
from rest_framework import viewsets, response, \
    permissions, decorators

from rna_seq.models.project import *
from api.serializers.project import *

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated,]

class ProjectManagerViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectManagerSerializer
    permission_classes = [permissions.IsAuthenticated,]