
from rest_framework import viewsets, response, permissions, decorators

from annot.models import Specie
from api.serializers import SpecieSerializer


class SpecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer
    permission_classes = [permissions.IsAuthenticated,]

