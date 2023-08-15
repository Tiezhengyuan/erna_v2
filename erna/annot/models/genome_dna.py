from django.db import models
from django.conf import settings
from django.core.files import File
from pathlib import Path
import os

from .specie import Specie

class GenomeDNAManager(models.Manager):
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

         
class GenomeDNA(models.Model):
    '''
    Genome DNA, one chromosome one fasta file
    '''
    specie = models.ForeignKey(Specie,
        on_delete=models.CASCADE)
    version = models.CharField(max_length=56)
    file_name = models.CharField(max_length=128)
    # str type from json format
    metadata = models.CharField(max_length=1256)

    objects = GenomeDNAManager()

    class Meta:
        app_label = 'annot'
        ordering = ['specie', 'version']

    @property
    def local_dir(self):
        return os.path.join(settings.DATA_DIR, 'genome_dna')
    
    @property
    def full_path(self):
        return os.path.join(self.local_dir, self.specie.specie_name, \
            self.version, self.file_name)

    def __str__(self):
         return self.specie.specie_name