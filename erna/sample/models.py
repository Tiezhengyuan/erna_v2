from django.db import models

# Create your models here.
from rna_seq.models.user import UserModel

class SampleModel(models.Model):
    profile_name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=256)
    creater = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        app_label = 'sample'
        # ordering = ('project_id',)


