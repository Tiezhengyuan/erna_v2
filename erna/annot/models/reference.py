
from django.db import models
from .genome import Genome

class ReferenceManager(models.Manager):
  def load_reference(self, genome, aligner, fa_path, index_path):
    data = {
      'fa_path': fa_path,
      'index_path': index_path,
    }
    res = self.update_or_create(genome=genome, aligner=aligner, \
      defaults = data)
    return res

class Reference(models.Model):
  genome = models.ForeignKey(
    Genome,
    related_name = 'references',
    on_delete=models.CASCADE
  )
  aligner = models.CharField(max_length= 10)
  fa_path = models.CharField(max_length=256)
  index_path = models.CharField(max_length=256)

  objects = ReferenceManager()

  class Meta:
    app_label = "annot"
    unique_together = ["genome", "aligner"]
    ordering = ["genome", "aligner"]
