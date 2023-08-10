from rest_framework import serializers

from rna_seq.models import Project, ProjectUser

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectUserSerializer(serializers.ModelSerializer):
    class Meata:
        model = ProjectUser
        fields = '__all__'