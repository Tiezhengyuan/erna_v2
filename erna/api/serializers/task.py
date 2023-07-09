from rest_framework import serializers
from rna_seq.models.task import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'


class TaskTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTreeModel
        fields = '__all__'

class TaskExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskExecutionModel
        fields = '__all__'