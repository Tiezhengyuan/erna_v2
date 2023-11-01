from rest_framework import serializers
from annot.models import *


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = '__all__'

class GenomeSerializer(serializers.ModelSerializer):
    annots = AnnotationSerializer(many=True)

    class Meta:
        model = Genome
        fields = ('specie', 'data_source', 'version', 'ftp_path', \
            'local_path', 'metadata', 'is_ready', 'annots')


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = '__all__'

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'