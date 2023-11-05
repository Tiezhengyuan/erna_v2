from rest_framework import serializers
from commons.models import *

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = '__all__'

class MethodToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodTool
        fields = '__all__'

class MethodRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodRelation
        fields = '__all__'


class MethodNameSerializer(serializers.ListSerializer):
    class Meta:
        model = Method
        fields = ['method_name',]