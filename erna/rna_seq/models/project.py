from django.db import models

# Create your models here.

from .user import UserModel

class ProjectModel(models.Model):
    project_id = models.CharField(primary_key=True,
        max_length=10, verbose_name="project ID")
    project_name = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE,
        verbose_name="owner identified by user_id")
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=526, blank=True)

    class Meta:
        app_label = 'rna_seq'
        ordering = ('project_id',)

    def __str__(self):
        return self.project_id

class ProjectManagerModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE,
        verbose_name="Executed project identified by project_id")
    manager = models.ForeignKey(UserModel, on_delete=models.CASCADE,
        verbose_name="executor identified by user_id")

    def __str__(self):
        return self.project.project_id

    