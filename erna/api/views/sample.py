from rest_framework import viewsets, response, permissions, decorators

from sample.models import Sample, SampleFile, SampleProject
from api.serializers import SampleSerializer, \
    SampleFileSerializer, SampleProjectSerializer

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
