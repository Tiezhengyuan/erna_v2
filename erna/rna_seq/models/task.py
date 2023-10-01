import json
from django.db import models
from django.core.serializers import serialize

# Create your models here.
from .project import Project
from commons.models import CustomUser, Tool

class TaskManager(models.Manager):
    def get_next_task_id(self, project_id):
        '''
        first confirm project_id, then consecutive on task_id
        '''
        project = Project.objects.get(project_id=project_id)
        last = self.model.objects.filter(project=project).last()
        if last:
            next_id = str(int(last.task_id[1:])+1)
            return f"T{next_id.zfill(2)}"
        return 'T01'
    
    def add_new_task(self, data):
        '''
        task_id could be generated automatically
        '''
        try:
            data['task_id'] = self.model.objects.get_next_task_id(data['project_id'])
            data['project_id'] = Project.objects.get(project_id=data['project_id']).id
            data['params'] = json.dumps(data.get('params', {}))
            task = self.model.objects.create(**data)
            task.save()
            return {'task_id': task.task_id}
        except Exception as e:
            print(e)
        return {}

    # def get_task(self, project_id, task_id):
    #     '''
    #     given a project_id , task_id is unique
    #     '''
    #     project = Project.objects.get_project_by_project_id(project_id)
    #     return self.model.objects.get(project=project, task_id=task_id)
    
    # def get_project_tasks(self, project_id):
    #     '''
    #     one project may include multiple tasks
    #     '''
    #     project = Project.objects.get_project_by_project_id(project_id)
    #     tasks = self.model.objects.filter(project=project)
    #     return tasks
    
    # def add_config(self, task_id, params, input, output:
    #     return self.model.objects.filter(task_id=task_id)\
    #         .update(params=params, input=input, \
    #                 output=output, is_ready=True)
    
    def delete_task(self, project_id, task_id):
        project = Project.objects.get_project_by_project_id(project_id)
        return self.model.objects.filter(project=project, task_id=task_id).delete()
    

class Task(models.Model):
    # project_id + task_id = pk
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task_id = models.CharField(
        unique=True,
        max_length=10,
        verbose_name="task ID"
    )
    task_name = models.CharField(
        max_length=100,
        blank=True,
        default = "task name",
        verbose_name="task name"
    )
    params = models.CharField(
        max_length=1256,
        blank=True, 
        verbose_name="parameters in json string"
    )
    is_ready = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    objects = TaskManager()

    class Meta:
        app_label = 'rna_seq'
        ordering = ('project', 'task_id',)
        unique_together = [
            ('project', 'task_id'),
        ]

    def __str__(self):
        return self.task_id

