from django.db import models

# Create your models here.
from .project import Project
from .tool import Tool
from .user import User

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
    
    def add_task(self, project_id, user_name, tool_name):
        '''
        task_id could be generated automatically
        '''
        task_id = self.model.objects.get_next_task_id(project_id)
        project = Project.objects.get_project_by_project_id(project_id)
        user = User.objects.get_user_by_user_name(user_name)
        tool = Tool.objects.get_last_version(tool_name)
        return self.model.objects.create(task_id=task_id,
            project=project, executor=user, tool=tool)

    def get_project_tasks(self, project_id):
        project = Project.objects.get_project_by_project_id(project_id)
        tasks = self.model.objects.filter(project=project)
        return tasks

    def add_config(self, task_id, params, input, output):
        return self.model.objects.filter(task_id=task_id)\
            .update(params=params, input=input, \
                    output=output, is_ready=True)
    
    def delete_task(self, task_id):
        return self.model.objects.filter(task_id=task_id).delete()
    

class Task(models.Model):
    # project_id + task_id = pk
    project = models.ForeignKey(Project,
        on_delete=models.CASCADE
    )
    task_id = models.CharField(
        unique=True,
        max_length=10,
        verbose_name="task ID"
    )
    executor = models.ForeignKey(User,
        on_delete=models.CASCADE
    )
    tool = models.ForeignKey(Tool,
        blank=True,
        on_delete=models.CASCADE
    )
    params = models.CharField(max_length=1256, blank=True, 
        verbose_name="parameters in json string")
    input = models.CharField(max_length=1256, blank=True,
        verbose_name="input metadata in json string")
    output = models.CharField(max_length=1256, blank=True,
        verbose_name="output metadata in json string")
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

