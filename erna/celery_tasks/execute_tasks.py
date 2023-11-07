'''
scheduled tasks:
search table Task and detect tasks with 'is_ready'=True
'''

from rna_seq.models import Project, Task

class ExecuteTasks:
    def __init__(self):
        pass
    
    def run_task(self, x=6, y=5):
        print(x, y)
        return x+y