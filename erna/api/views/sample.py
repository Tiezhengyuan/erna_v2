from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from rest_framework import viewsets, response, permissions, decorators
from sample.models import *
from api.serializers import *
       
class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = [permissions.IsAuthenticated]

class SampleFileViewSet(viewsets.ModelViewSet):
    queryset = SampleFile.objects.all()
    serializer_class = SampleFileSerializer
    permission_classes = [permissions.IsAuthenticated]

class SampleProjectViewSet(viewsets.ModelViewSet):
    queryset = SampleProject.objects.all()
    serializer_class = SampleProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
