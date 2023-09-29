

from django.urls import path,include
from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()
# app: rna_seq
router.register('project', ProjectViewSet, basename='project')
router.register('project_user', ProjectUserViewSet, basename='project_user')
router.register('task', TaskViewSet, basename='task')
router.register('task_tree', TaskViewSet, basename='task_tree')
router.register('task_execution', TaskViewSet, basename='task_execution')

# app: commons
router.register('user', CustomUserViewSet, basename='user')
# router.register('current_user', CustomUserViewSet.get_object, basename='current_user')
router.register('tool', ToolViewSet, basename='tool')

# app: sample
router.register('sample', SampleViewSet, basename='sample')
router.register('sample_file', SampleFileViewSet, basename='sample_file')
router.register('sample_project', SampleProjectViewSet, basename="sample_project")

#app: annotation
router.register('specie', SpecieViewSet, basename='specie')
router.register('genome', GenomeViewSet, basename='genome')
router.register('annotation', AnnotationViewSet, basename='annotation')
router.register('reference', ReferenceViewSet, basename='reference')

#celery tasks
router.register('celery_task_result', TaskResultViewSet, basename='celery_task_result')

urlpatterns = [
    path('', include(router.urls)),
]