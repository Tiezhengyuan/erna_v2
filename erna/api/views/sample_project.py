from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from rest_framework import viewsets, permissions
from sample.models import Sample, SampleProject
from api.serializers import SampleSerializer, SampleProjectSerializer
       
class SampleProjectViewSet(viewsets.ModelViewSet):
    queryset = SampleProject.objects.all()
    serializer_class = SampleProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
