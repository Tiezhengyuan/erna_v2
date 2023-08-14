from rest_framework import serializers
from sample.models import Sample

class SampleSerializer(serializers.ModelSerializer):
    class meta:
        model = Sample
        fields = '__all__'