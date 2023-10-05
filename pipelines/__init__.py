import os
import sys
DIR_PROJECT = os.path.dirname(os.path.dirname(__file__))
DIR_DJANGO = os.path.join(DIR_PROJECT, 'erna')

sys.path.append(DIR_DJANGO)