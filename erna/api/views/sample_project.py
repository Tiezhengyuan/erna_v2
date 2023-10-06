from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from rest_framework import viewsets, permissions
from sample.models.sample_project import SampleProject
from api.serializers import SampleProjectSerializer
       
class SampleProjectViewSet(viewsets.ModelViewSet):
    queryset = SampleProject.objects.all()
    serializer_class = SampleProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
