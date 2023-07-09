from rest_framework import serializers

from rna_seq.models.project import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'

class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meata:
        model = ProjectManagerModel
        fields = '__all__'