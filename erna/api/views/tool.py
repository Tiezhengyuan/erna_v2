
from rest_framework import viewsets, response, permissions, decorators
from rna_seq.models.tool import *
from api.serializers.tool import *

class ToolViewSet(viewsets.ModelViewSet):
    queryset = ToolModel.objects.all()
    serializer_class = ToolSerializer
    permission_classes = [permissions.IsAuthenticated]