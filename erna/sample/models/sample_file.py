'''
one file one record.
'''
from django.db import models
from django.conf import settings
import os
from typing import Iterable
from .sample import Sample
from .raw_data import RawData

class SampleFileManager(models.Manager):

    def iterate_raw_data(self, study_name:str)->Iterable:
        '''
        Iteration of all files defined in RawData
        given a study name defined in Sample
        '''
        samples = Sample.objects.filter(study_name=study_name)
        for sample in samples:
            sample_files = self.filter(sample=sample)
            for sample_file in sample_files:
                raw_data = sample_file.raw_data
                yield sample, raw_data, sample_file
                 
    def get_study_files(self, study_name:str):
        '''
        get relations of sample~sample file given a study_name
        '''
        res = {}
        iter = self.iterate_raw_data(study_name)
        for sample, raw_data, sample_file in iter:
            sample_name = sample.sample_name
            if sample_name not in res:
                res[sample_name] = {
                    'sample_file_id': sample_file.id,
                    'sample_id': sample.id,
                    'sample_name': sample_name,
                    'raw_data': [],
                }
            sample_file = raw_data.to_dict()
            res[sample_name]['raw_data'].append(sample_file)
        return res

    def add_sample_file(self, sample_file:dict):
        '''
        post a new record
        '''
        file_obj = self.model.objects.create(
            sample_id=sample_file['sample'],
            raw_data_id=sample_file['raw_data']
        )
        file_obj.save()
        return file_obj
    
    def get_sample_files(self, sample_name:str):
        '''
        one sample may include 0-many files
        '''
        try:
            sample = Sample.objects.get(sample_name=sample_name)
            return self.model.objects.filter(sample=sample.id)
        except Exception as e:
            pass
        return []


class SampleFile(models.Model):
    # one sample may include multiple files
    sample = models.ForeignKey(
        Sample,
        on_delete = models.CASCADE
    )
    # path of raw data
    raw_data = models.ForeignKey(
        RawData,
        on_delete = models.CASCADE
    )

    objects = SampleFileManager()

    class Meta:
        app_label = 'sample'
        ordering = ('sample', 'raw_data')

    def get_sample(self):
        res = Sample.objects.get(id=self.sample.id)
        return res.to_dict()
    
    def get_raw_data(self):
        res = RawData.objects.get(id=self.raw_data.id)
        return res.to_dict()
