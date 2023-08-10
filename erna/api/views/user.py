from rest_framework import viewsets, response, permissions, decorators

from rna_seq.models import User
from api.serializers.user import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]