from django.db import models
from rna_seq.models import Project
from .specie import Specie

class ReferenceManager(models.Manager):
  def get_reference_path(self, project_id:str):
    pass

class Reference(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
  data_source = models.CharField(
    max_length=10,
    default = "NCBI",
    choices=[
      ('NCBI', 'NCBI'),
      ('ENSEMbL', 'ENSEMbL'),
      ('other', 'other'),
    ] 
  )
  data_path = models.CharField(
    max_length=512,
    default = ""
  )

  objects = ReferenceManager()

  class Meta:
    app_label = "annot"
    ordering = ["project", "specie",]
