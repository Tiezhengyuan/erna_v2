from rest_framework import viewsets, response, permissions, decorators

from commons.models import Method
from api.serializers import MethodSerializer

class MethodViewSet(viewsets.ModelViewSet):
    serializer_class = MethodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        method_name = self.request.query_params.get('method_name', None)
        if method_name is not None:
            return Method.objects.get_method_tools(method_name)
        return Method.objects.all()
