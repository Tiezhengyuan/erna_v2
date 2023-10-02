from django.db import models
from django.conf import settings
from django.core.files import File
from pathlib import Path
import os

from .specie import Specie

class GenomeManager(models.Manager):
    def get_genome(self, specie_name:str, version:str=None):
        specie = Specie.objects.get(specie_name=specie_name)
        if version is None:
            return self.filter(specie=specie).last()
        return self.get(specie=specie, version=version)
    
    def get_versions(self, specie_name:str):
            specie = Specie.objects.get(specie_name=specie_name)
            query = self.filter(specie=specie)
            return [i.version for i in query]

    def get_files_path(self, specie_name:str, version:str=None):
        last = self.get_genome(specie_name, version)
        files = self.filter(specie=last.specie)
        return [f.full_path for f in files]

         
class Genome(models.Model):
    '''
    Genome DNA, one chromosome one fasta file
    '''
    specie = models.ForeignKey(
        Specie,
        on_delete=models.CASCADE
    )
    version = models.CharField(max_length=56)
    data_path = models.CharField(max_length=512)
    data_source = models.CharField(
        max_length=10,
        default = "NCBI",
        choices=[
            ('NCBI', 'NCBI'),
            ('ENSEMbL', 'ENSEMbL'),
            ('other', 'other'),
        ] 
    )
    # str type from json format
    metadata = models.CharField(
        max_length=1256,
        blank=True,
        null=True
    )

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
        return os.path.join(self.specie.specie_name, self.version, self.file_name)

    @property
    def full_path(self):
        return os.path.join(self.local_dir, self.sub_dir)

    def __str__(self):
         return self.specie.specie_name