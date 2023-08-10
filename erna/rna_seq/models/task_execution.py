
from django.db import models
from .task import Task

class TaskExecution(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        choices=[
            ('S', 'suspend'),
            ('R', 'running'),
            ('D', 'finished'),
            ('F', 'failed'),
        ],
        max_length=10
    )
    command = models.CharField(
        max_length=1256,
        verbose_name="command for tool launching"
    )
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    class Meta:
        app_label = 'rna_seq'
        # ordering = ('task',)
