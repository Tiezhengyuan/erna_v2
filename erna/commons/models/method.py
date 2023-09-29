from django.db import models
import itertools
from .tool import Tool

class MethodManager(models.Manager):
  def get_method_tools(self, method_name:str):
    '''
    get all tools given a method_type
    '''
    return self.model.objects.filter(method_name=method_name).order_by('tool')
  
  def get_methods(self):
    '''
    retrieve all methods
    '''
    return self.model.objects.values_list('method_name', flat=True).distinct()


class Method(models.Model):
  method_name = models.CharField(
    max_length=20,
    choices = [
      ('GAL', 'genome alignment'),
      ('DSA', 'DNA sequence alignment'),
      ('GAS', 'genome assembly'),
      ('CR', 'count reads'),
      ('TS', 'trim sequences'),
      ('QC', 'quality control'),
      ('CFF', 'convert file format'),
    ]
  )
  tool = models.ForeignKey(
    Tool,
    on_delete=models.CASCADE
  )
  description = models.CharField(
    max_length=526,
    blank=True,
    null=True
  )

  objects = MethodManager()

  class Meta:
    app_label = 'commons'
    ordering = ['method_name', 'tool']