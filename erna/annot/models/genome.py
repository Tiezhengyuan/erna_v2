import os
import json
from django.db import models
from django.conf import settings
from django.core.files import File
from pathlib import Path

from .specie import Specie

class GenomeManager(models.Manager):
    def get_genome(self, organism_name:str, version:str=None):
        specie = Specie.objects.get(organism_name=organism_name)
        if version is None:
            return self.filter(specie=specie).last()
        return self.get(specie=specie, version=version)
    
    def get_versions(self, organism_name:str):
            specie = Specie.objects.get(organism_name=organism_name)
            query = self.filter(specie=specie)
            return [i.version for i in query]

    def get_ftp_path(self, specie:str, version:str=None):
        obj = self.get(specie=specie, version=version)
        return obj.ftp_path


    def load_genome(self, data:dict):
        '''
        post new genome or update metadata of the genome
        '''
        if 'specie' in data and 'version' in data:
            if 'metadata' in data:
                data['metadata'] = json.dumps(data['metadata'])
            existing = Genome.objects.filter(specie=data['specie'],\
                version=data['version'])
            if not existing:
                data['specie'] = Specie.objects.get(organism_name=data['specie'])
                return Genome.objects.create(**data)
            else:
                if 'metadata' in data:
                    return existing.update(metadata=data['metadata'])
        return None

         
class Genome(models.Model):
    '''
    Genome DNA, one chromosome one fasta file
    '''
    specie = models.ForeignKey(
        Specie,
        on_delete=models.CASCADE
    )
    data_source = models.CharField(
        max_length=10,
        default = "NCBI",
        choices=[
            ('NCBI', 'NCBI'),
            ('ENSEMBL', 'ENSEMBL'),
            ('other', 'other'),
        ] 
    )
    version = models.CharField(max_length=56)
    ftp_path = models.CharField(
        max_length=512,
        blank=True,
        null=True
    )
    # str type from json format
    metadata = models.CharField(
        max_length=1256,
        blank=True,
        null=True
    )
    is_ready = models.BooleanField(default=False)

    objects = GenomeManager()

    class Meta:
        app_label = 'annot'
        unique_together = ('specie', 'version')
        ordering = ['specie', 'version']

    @property
    def local_dir(self):
        return os.path.join(settings.DATA_DIR, self.label)

    @property
    def sub_dir(self):
        return os.path.join(self.specie.organism_name, self.version, self.file_name)

    @property
    def full_path(self):
        return os.path.join(self.local_dir, self.sub_dir)

    def __str__(self):
         return self.specie.organism_name