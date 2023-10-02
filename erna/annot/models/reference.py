from django.db import models
from rna_seq.models import Project
from .genome import Genome

class Reference(models.Model):
  project = models.ForeignKey(
    Project,
    on_delete=models.CASCADE
  )
  genome = models.ForeignKey(
    Genome,
    on_delete=models.CASCADE
  )

  class Meta:
    app_label = "annot"
    ordering = ["genome", "project"]
