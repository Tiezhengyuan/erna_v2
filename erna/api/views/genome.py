
from rest_framework import viewsets, response, permissions, decorators

from annot.models import Genome
from api.serializers import GenomeSerializer


class GenomeViewSet(viewsets.ModelViewSet):
    queryset = Genome.objects.all()
    serializer_class = GenomeSerializer
    permission_classes = [permissions.IsAuthenticated]
