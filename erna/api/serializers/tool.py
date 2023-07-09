from rest_framework import serializers
from rna_seq.models.tool import *

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolModel
        fields = '__all__'