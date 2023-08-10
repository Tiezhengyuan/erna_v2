
from rest_framework import viewsets, response, permissions, decorators
from rna_seq.models import Tool
from api.serializers.tool import *

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    permission_classes = [permissions.IsAuthenticated]