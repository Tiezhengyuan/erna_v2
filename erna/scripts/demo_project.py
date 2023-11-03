import json
from rna_seq.models import Project, Task, TaskExecution
from commons.models import CustomUser
from sample.models import SampleProject Sample, SampleFile, 

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
        'task_name': '',
        'params': {
            'method': 'build_index',
            'data_source': 'NCBI',
            'specie': 'Homo sapiens',
            'version': 'GCF_000001405.40',
            'aligner': 'hisat2',
            'child': ['T002'],
        },
        'is_ready': True,
    },
    {
        'task_id': 'T002',
        'task_name': '',
        'params': {
            'method': 'genome_alignment',
            'aligner': 'hisat2',
            'index_path': 'aaa',
            'parent': ['T001'],
            'child': ['T003'],
        },
        'is_ready': False,
    },
    {
        'task_id': 'T003',
        'task_name': '',
        'params': {
            'method': 'assemble_transcripts',
            'assembler': 'hisat2',
            'parent': ['T002'],
            'child': ['T004'],
        },
        'is_ready': False,
    },
    {
        'task_id': 'T004',
        'task_name': '',
        'params': {
            'method': 'count_reads',
            'parent': ['T003'],
        },
        'is_ready': False,
    },

]
for task in tasks:
    task['project'] = project
    task['params'] = json.dumps(task['params'])
    task_obj = Task.objects.create(**task)
    print(task_obj)

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
