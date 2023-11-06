'''
example:
    python3 erna/manage.py shell < erna/scripts/demo_project.py
'''
import json
from rna_seq.models import *
from commons.models import CustomUser


user = CustomUser.objects.get(pk=1)
project_id = "P00001"

# cretae project
new_project = {
    "project_id": project_id,
    "project_name": "test_mrna_seq",
    "description": "for testing mRNA-seq",
    "status": "A",
    "sequencing": "M",
    'owner': user

}
Project.objects.filter(project_id=project_id).delete()
project = Project.objects.create(**new_project)
print(project)

# add tasks
tasks = [
    {
        'task_id': 'T001',
        'task_name': 'build index',
        'method_name': 'build_index',
        'tool_name': 'hisat2-build',
        'params': {
            'data_source': 'NCBI',
            'specie': 'Homo sapiens',
            'version': 'GCF_000001405.40',
        },
        'child': ['T002'],
        'is_ready': True,
    },
    {
        'task_id': 'T002',
        'task_name': '',
        'method_name': 'align_transcriptome',
        'tool_name': 'hisat2',
        'params': {
            'index_path': 'aaa',
        },
        'parent': ['T001'],
        'child': ['T003'],
        'is_ready': False,
    },
    {
        'task_id': 'T003',
        'task_name': '',
        'method_name': 'assemble_transcripts',
        'tool_name': 'stringtie',
        'params': {},
        'parent': ['T002'],
        'child': ['T004'],
        'is_ready': False,
    },
    {
        'task_id': 'T004',
        'task_name': '',
        'method_name': 'count_reads',
        'parent': ['T003'],
        'is_ready': False,
    },
    {
        'task_id': 'T006',
        'is_ready': False,
    },
]
for task in tasks:
    # update Task
    method_tool = MethodTool.objects.get_method_tool(
        task['method_name'], task.get('tool_name'), task.get('version')
    ) if 'method_name' in task else None
    task_obj = Task.objects.create(project=project, \
        method_tool=method_tool, task_id=task['task_id'], \
        task_name= task.get('task_name'), \
        params=json.dumps(task.get('params', {})), \
        is_ready=task.get('id_ready', False))
    print(task_obj, task_obj.id)

samples = {
    'sample_1': {
        'R1': 'sample_1_R1.fastq',
        'R2': 'sample_1_R2.fastq',
    },
    'sample_2': {
        'R1': 'sample_2_R1.fastq',
        'R2': 'sample_2_R2.fastq',
    }
}
