'''

'''
from django.db import models
from .method import Method
from .constants import METHODS


class MethodRelationManager(models.Manager):
  def refresh_methods(self):
    self.all().delete()
    res = []
    for method in METHODS:
      name = method['method_name']
      for child in method['child_method']:
        obj = self.create(
          method=Method.objects.get(method_name=name),
          child=Method.objects.get(method_name=child)
        )
        res.append(obj)
    return res

class MethodRelation(models.Model):
  method = models.ForeignKey(
    Method,
    on_delete=models.CASCADE
  )
  child = models.ForeignKey(
    Method,
    related_name = 'child_methods',
    on_delete=models.CASCADE
  )

  objects = MethodRelationManager()

  class Meta:
    app_label = 'commons'
    ordering = ['method', 'child']