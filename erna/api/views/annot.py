
from rest_framework import viewsets, response, permissions, decorators

from annot.models import Specie, Genome, Annotation
from api.serializers import SpecieSerializer, GenomeSerializer, AnnotationSerializer


class SpecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer
    permission_classes = [permissions.IsAuthenticated,]

class GenomeViewSet(viewsets.ModelViewSet):
    queryset = Genome.objects.all()
    serializer_class = GenomeSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = [permissions.IsAuthenticated]

