from rest_framework import serializers
from sample.models import *

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'

class SampleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleFile
        fields = '__all__'

class SampleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleProject
        fields = '__all__'