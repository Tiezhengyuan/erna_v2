from ddt import ddt, data, unpack
from django.test import TestCase
from rna_seq.models import  ProjectModel, ProjectManagerModel, UserModel

@ddt
class TestProjectModel(TestCase):
    
    def setUp(self):
        user = UserModel.objects.create(user_name="tester", status="ative")
        ProjectModel.objects.create(project_name='test1', owner=user)
        # ProjectModel.objects.create(project_name='test2', owner=user)

    @data(
        ['test1', 'test1', 'tester'],
    )
    @unpack
    def test_project_model(self, project_name, expect_name, expect_user):
        res = ProjectModel.objects.get(project_name=project_name)
        assert res.project_name == expect_name
        assert str(res.owner) == expect_user
        print(f'\n###{res.project_id}###')

