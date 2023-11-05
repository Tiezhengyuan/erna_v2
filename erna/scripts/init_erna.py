'''
initialize models
example:
    python3 erna/manage.py shell < scripts/init_db.py
'''
from rna_seq.models import *
from process.process_raw_data import ProcessRawData


# refresh RawData
RawData.objects.all().delete()
raw_data = ProcessRawData().scan_raw_data()
data = RawData.objects.load_data(raw_data)

# refresh Method
methods = Method.objects.refresh_methods()

# refresh Tool
tools = Tool.objects.refresh()

# refresh MethodTool
method_tools = MethodTool.objects.refresh()

# refresh MethodRelation
method_relations = MethodRelation.objects.refresh()



