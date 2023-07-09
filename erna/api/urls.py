

from django.urls import path,include
from rest_framework import routers

from api.views.project import *
from api.views.task import *
from api.views.tool import *
from api.views.user import *
from api.views.sample import *

router = routers.DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('project_manager', ProjectManagerViewSet, basename='project_manager')
router.register('task', TaskViewSet, basename='task')
router.register('task_tree', TaskViewSet, basename='task_tree')
router.register('task_execution', TaskViewSet, basename='task_execution')
router.register('tool', ToolViewSet, basename='tool')
router.register('user', UserViewSet, basename='user')
router.register('sample', SampleViewSet, basename='sample')


urlpatterns = [
    path('', include(router.urls)),
]