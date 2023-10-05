import os

DIR_TESTS = os.path.dirname(__file__)
DIR_PIPELINES = os.path.dirname(DIR_TESTS)
DIR_RAW_DATA = os.path.join(DIR_PIPELINES, 'raw_data')
DIR_RESULTS = os.path.join(DIR_PIPELINES, 'results')
DIR_REFERENCES = os.path.join(DIR_PIPELINES, 'references')