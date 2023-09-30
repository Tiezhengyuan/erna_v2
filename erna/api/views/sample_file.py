from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from rest_framework import viewsets, permissions
from sample.models import SampleFile
from api.serializers import SampleFileSerializer
       
class SampleFileViewSet(viewsets.ModelViewSet):
    queryset = SampleFile.objects.all()
    serializer_class = SampleFileSerializer
    permission_classes = [permissions.IsAuthenticated]
