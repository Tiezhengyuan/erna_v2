from rest_framework import serializers
from sample.models.raw_data import RawData
from sample.models.sample import Sample
from sample.models.sample_file import SampleFile
from sample.models.sample_project import SampleProject

class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = '__all__'

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
