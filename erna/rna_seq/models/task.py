from django.db import models

# Create your models here.
from .project import ProjectModel, ProjectManagerModel
from .tool import ToolModel

class TaskModel(models.Model):
    task_id = models.CharField(primary_key=True, max_length=10,
        verbose_name="task ID")
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    tool = models.ForeignKey(ToolModel, on_delete=models.CASCADE)
    paramters = models.CharField(max_length=1256,
        verbose_name="parameters in json string")
    input = models.CharField(max_length=1256,
        verbose_name="input metadata in json string")
    output = models.CharField(max_length=1256,
        verbose_name="output metadata in json string")
    is_ready = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'rna_seq'
        ordering = ('task_id',)

    def __str__(self):
        return self.task_id

class TaskTreeModel(models.Model):
    parent_task = models.ForeignKey(TaskModel, on_delete=models.CASCADE,
        related_name='parent_task')
    child_task = models.ForeignKey(TaskModel, on_delete=models.CASCADE,
        related_name='child_task')

    class Meta:
        app_label = 'rna_seq'


class TaskExecutionModel(models.Model):
    EXE_STATUS = [
        ('S', 'suspend'),
        ('R', 'running'),
        ('D', 'finished'),
        ('F', 'failed'),
    ]
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    executor = models.ForeignKey(ProjectManagerModel,
        on_delete=models.CASCADE)
    status = models.CharField(choices=EXE_STATUS, max_length=10)
    command = models.CharField(max_length=1256,
        verbose_name="command for tool launching")
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    class Meta:
        app_label = 'rna_seq'
        ordering = ('task',)
