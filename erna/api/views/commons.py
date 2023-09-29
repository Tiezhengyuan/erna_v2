from rest_framework import viewsets, response, permissions, decorators

from commons.models import CustomUser, Tool, Method
from api.serializers import *

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk == "current":
            return self.request.user
        return super().get_object()

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    permission_classes = [permissions.IsAuthenticated]

class MethodViewSet(viewsets.ModelViewSet):
    serializer_class = MethodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        method_name = self.request.query_params.get('method_name', None)
        if method_name is not None:
            return Method.objects.get_method_tools(method_name)
        return Method.objects.all()

# todo debugging in the future
class MethodNameViewSet(viewsets.ModelViewSet):
    queryset = Method.objects.values_list('method_name', flat=True).distinct()
    serializer_class = MethodNameSerializer
    permission_classes = [permissions.IsAuthenticated]