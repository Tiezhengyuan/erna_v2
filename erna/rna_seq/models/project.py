from django.db import models
from django.conf import settings
from commons.models import CustomUser

class ProjectManager(models.Manager):

    def get_last_project_id(self):
        return self.model.objects.last().project_id

    def get_next_project_id(self):
        last = self.model.objects.last()
        if last:
            next_id = str(int(last.project_id[1:]) + 1)
            return f"P{next_id.zfill(5)}"
        return f"P00001"

    def get_project_by_project_id(self, project_id:str):
        '''
        get projects by project_id
        '''
        return self.model.objects.get(project_id=project_id, status='A')

    def get_project_by_project_name(self, project_name:str):
        '''
        get projects by project_name
        '''
        return self.model.objects.filter(project_name=project_name, status='A')

    def get_project_by_owner_name(self, user_name:str):
        '''
        get projects by user name
        '''
        try:
            owner = CustomUser.objects.get(user_name=user_name)
            projects = self.model.objects.filter(owner=owner, status='A')
            return projects
        except Exception as e:
            print(e)
        return None
        
    def insert(self, data:dict):
        '''
        insert a new project
        '''
        data['project_id'] = self.model.objects.get_next_project_id()
        Project.objects.create(**data)
        return data['project_id']
   
    def delete(self, project_id):
        return Project.objects.filter(project_id=project_id).update(status='D')


class Project(models.Model):
    project_id = models.CharField(
        max_length= 10,
        default = 'P00001',
        unique=True,
        verbose_name="project ID"
    )
    project_name = models.CharField(
        max_length=50,
        blank=True
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="owner identified by user_id"
    )
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(
        max_length=526,
        blank=True
    )
    status = models.CharField(
        max_length=1,
        choices=[('A', 'active'), ('D', 'deleted')],
        default='A',
    )

    objects = ProjectManager()

    class Meta:
        app_label = 'rna_seq'
        ordering = ['project_id',]

    def __str__(self):
        return self.project_id
    

    