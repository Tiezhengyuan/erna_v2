from rest_framework import serializers
from sample.models import *

class SampleSerializer(serializers.ModelSerializer):
    class meta:
        model = SampleModel
        fields = '__all__'