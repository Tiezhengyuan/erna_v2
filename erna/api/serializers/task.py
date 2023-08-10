from rest_framework import serializers
from rna_seq.models import *

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