import os
from django.db import models
from django.conf import settings
from .genome import Genome, GenomeManager, Specie

class AnnotationManager(GenomeManager):
    def get_annotation(self, specie_name:str, seq_type:str, version:str=None):
        specie = Specie.objects.get(specie_name=specie_name)
        if version is None:
            return self.filter(specie=specie, seq_type=seq_type).last()
        return self.get(specie=specie, assembly_accession=version, seq_type=seq_type)

class Annotation(Genome):
    label = 'annotations'
    file_format = models.CharField(
        max_length=10,
        choices=[
            ('FQ', 'FASTQ'),
            ('FA', 'FASTA'),
            ('GBK', 'GBK'),
            ('BAT', 'BAT'),
            ('SAM', 'SAM'),
            ('BAM', 'BAM'),
            ('O', 'other'),
        ]
    )
    seq_type = models.CharField(
        max_length=10,
        choices=[
            ('R', 'RNA'),
            ('D', 'DNA'),
            ('P', 'protein'),
            ('O', 'other'),
        ])

    objects = AnnotationManager()

    class Meta:
        # unique_together = ('specie', 'assembly_accession', 'seq_type')
        ordering = ['specie', 'assembly_accession', 'seq_type']