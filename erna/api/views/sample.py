from rest_framework import viewsets, response, permissions, decorators

from rna_seq.models import User
from api.serializers.sample import *

class SampleViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SampleSerializer
    permission_classes = [permissions.IsAuthenticated]