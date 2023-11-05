'''

'''
from django.db import models
from .tool import Tool
from .constants import METHODS
from .method import Method

class MethodToolManager(models.Manager):
  def refresh(self):
    self.all().delete()
    res = []
    for method in METHODS:
      method_obj = Method.objects.get(method_name=method['method_name'])
      for tool_name in method['tool_name']:
        tools = Tool.objects.filter(tool_name=tool_name)
        for tool in tools:
          obj = self.create(method=method_obj, tool = tool)
          res.append(obj)
    return res

class MethodTool(models.Model):
  method = models.ForeignKey(
    Method,
    related_name = 'tools',
    on_delete=models.CASCADE
  )
  tool = models.ForeignKey(
    Tool,
    related_name = 'methods',
    on_delete=models.CASCADE
  )

  objects = MethodToolManager()

  class Meta:
    app_label = 'rna_seq'
    unique_together = ['method', 'tool']
    ordering = ['method', 'tool']