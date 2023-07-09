
from rest_framework import viewsets, response, permissions, decorators
from rna_seq.models.task import *
from api.serializers.task import *

class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskTreeSet(viewsets.ModelViewSet):
    queryset = TaskTreeModel.objects.all()
    serializer_class = TaskTreeSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskExecutionViewSet(viewsets.ModelViewSet):
    queryset = TaskExecutionModel.objects.all()
    serializer_class = TaskExecutionSerializer
    permission_classes = [permissions.IsAuthenticated]
