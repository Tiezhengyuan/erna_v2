from rest_framework import serializers

from rna_seq.models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectUserSerializer(serializers.ModelSerializer):
    class Meata:
        model = ProjectUser
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTree
        fields = '__all__'

class TaskExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskExecution
        fields = '__all__'

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
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


# class MethodNameSerializer(serializers.ListSerializer):
#     class Meta:
#         model = Method
#         fields = ['method_name',]