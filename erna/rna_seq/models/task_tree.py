from typing import Iterable
from django.db import models

from .task import Task

class TaskTreeManager(models.Manager):

    def get_tasks(self, task_id:str):
        '''
        multiple rows given a task_id
        '''
        task = Task.objects.get(task_id=task_id)
        return self.model.objects.filter(task=task)
    
    def get_parents(self, task_id:str):
        '''
        one task may have multiple parents
        '''
        parents = []
        tasks = self.model.objects.get_tasks(task_id)
        for t in tasks:
            parents.append(t.parent)
        return parents

    def get_children(self, task_id:str):
        '''
        one task may have multiple children
        '''
        children = []
        tasks = self.model.objects.get_tasks(task_id)
        for t in tasks:
            children.append(t.child)
        return children
    
    def BFS(self, task_id)->Iterable:
        '''
        task_id is root task
        '''
        i, pool = 0, [task_id]
        while i < len(pool):
            task_id = pool[i]
            task = Task.objects.get(task_id=task_id)
            children = self.model.objects.get_children(task_id)
            for t in children:
                if t not in pool:
                    pool.append(t)
            i += 1
            yield task, children




class TaskTree(models.Model):
    task = models.ForeignKey(Task,
        on_delete=models.CASCADE,
        related_name='current_task'
    )
    parent = models.ForeignKey(Task,
        black=True,
        on_delete=models.CASCADE,
        related_name='parent_task'
    )
    child = models.ForeignKey(Task,
        blank=True,
        on_delete=models.CASCADE,
        related_name='child_task'
    )

    objects = TaskTreeManager()

    class Meta:
        app_label = 'rna_seq'
        ordering = ('task',)
