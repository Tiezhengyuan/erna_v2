from rest_framework import viewsets, response, permissions, decorators

from sample.models import *
from api.serializers.sample import *

class SampleViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = SampleSerializer
    permission_classes = [permissions.IsAuthenticated]