from typing import Iterable
from django.db import models

from .task import Task
from .project import Project

class TaskTreeManager(models.Manager):

    def get_tasks(self, project_id:str, task_id:str):
        task = Task.objects.get_task(project_id, task_id)
        return task, self.model.objects.filter(task=task)

    def get_parents(self, project_id:str, task_id:str):
        '''
        one task may have multiple parents
        '''
        parents = []
        task, tasks = self.model.objects.get_tasks(project_id, task_id)
        for t in tasks:
            parents.append(t.parent)
        return task, parents

    def get_children(self, project_id:str, task_id:str):
        '''
        one task may have multiple children
        '''
        children = []
        task, tasks = self.model.objects.get_tasks(project_id, task_id)
        for t in tasks:
            children.append(t.child)
        return task, children
    
    def BFS(self, project_id:str, task_id:str)->Iterable:
        '''
        task_id is root task. Given task_id,
        search all children using breadth-first search 
        '''
        i, pool = 0, [task_id]
        while i < len(pool):
            task_id = pool[i]
            task, children = self.model.objects.get_children(project_id, task_id)
            for child in children:
                if child and child not in pool:
                    pool.append(child)
                    yield task, child
            i += 1

    def append_task(self, project_id:str, task_id:str, parent_task_id=None):
        '''
        suppose both tasks exist
        '''
        task = Task.objects.get_task(project_id, task_id)
        # is root node
        if parent_task_id is None:
            return self.model.objects.create(task=task)
        # is child node
        parent = Task.objects.get_task(project_id, parent_task_id)
        self.model.objects.create(task=parent, child=task)
        return self.model.objects.create(task=task, parent=parent)



class TaskTree(models.Model):
    '''
    task, parent and child must belong to same project
    '''
    task = models.ForeignKey(Task,
        on_delete=models.CASCADE,
        related_name='current_task'
    )
    parent = models.ForeignKey(Task,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='parent_task'
    )
    child = models.ForeignKey(Task,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='child_task'
    )

    objects = TaskTreeManager()

    class Meta:
        app_label = 'rna_seq'
        ordering = ('task',)
    
    def __str__(self):
        return self.task.task_id
