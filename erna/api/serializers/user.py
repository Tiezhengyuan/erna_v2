from rest_framework import serializers
from rna_seq.models.user import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'