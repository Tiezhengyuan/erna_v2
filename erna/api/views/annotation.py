
from rest_framework import viewsets, response, permissions, decorators

from annot.models import Specie, Genome, Annotation, Reference
from api.serializers import AnnotationSerializer


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = [permissions.IsAuthenticated]

