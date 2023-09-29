from rest_framework import viewsets, response, permissions, decorators
from sample.models import *
from api.serializers import *

class RawDataViewSet(viewsets.ModelViewSet):
    serializer_class = RawDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        batch_name = self.request.query_params.get('batch_name', None)
        if batch_name is not None:
            return RawData.objects.get_batch_files(batch_name)
        return RawData.objects.all()
    
class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = [permissions.IsAuthenticated]

class SampleFileViewSet(viewsets.ModelViewSet):
    queryset = SampleFile.objects.all()
    serializer_class = SampleFileSerializer
    permission_classes = [permissions.IsAuthenticated]

class SampleProjectViewSet(viewsets.ModelViewSet):
    queryset = SampleProject.objects.all()
    serializer_class = SampleProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
