from ddt import ddt, data, unpack
import json
import os
from django.test import TestCase, override_settings
from rna_seq.models import User, Project,Tool, Task, TaskTree

@ddt
class TestTaskTree(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_name="tester",
            email="a@abc.com",
            password="pass"
        )
        self.project = Project.objects.create(
            project_id='P00001',
            project_name='test1',
            owner=self.user
        )
        self.tool = Tool.objects.create(
            tool_name='Bowtie',
            tool_path = 'bowtie/3.4.5',
            version = '3.4.5',
        )
        self.task1 = Task.objects.add_task(
            project = self.project,
            executor=self.user,
            tool=self.tool
        )
        self.task2 = Task.objects.add_task(
            project = self.project,
            executor=self.user,
            tool=self.tool
        )
        self.task2 = Task.objects.add_task(
            project = self.project,
            executor=self.user,
            tool=self.tool
        )

    def test_CRUD(self):
        res = TaskTree.objects.create(
            task_id='T01',
            project = self.project,
            executor=self.user,
            tool=self.tool
        )
        assert str(res) == 'T01'

        # get
        res = TaskTree.objects.get(project=self.project)
        assert res.executor.user_name == 'tester'
        res = TaskTree.objects.get(executor=self.user)
        assert resTree.project.project_name == 'test1'

        # # udpate
        # new_project = Project.objects.create(
        #     project_id='P00002',
        #     project_name='test1',
        #     owner=self.user
        # )
        # res = TaskTree.objects.filter(project=self.project)\
        #     .update(project=new_project)
        # assert res == 1

        # # delete
        # res = TaskTree.objects.filter(project=self.project).delete()
        # assert res[0] == 0
        # res = TaskTree.objects.filter(project=new_project).delete()
        # assert res[0] == 1