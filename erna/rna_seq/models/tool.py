from django.db import models

# Create your models here.


class ToolModel(models.Model):
    tool_name = models.CharField(max_length=100)
    tool_path = models.CharField(max_length=256)
    default_parameters = models.CharField(max_length=1000,
        verbose_name='default parameters of the tool')
    create_time = models.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=20, blank=True)
    download_url = models.CharField(max_length=512, blank=True)

    class Meta:
        app_label = 'rna_seq'