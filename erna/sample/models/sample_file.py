'''
one file one record.
'''
from django.db import models
from django.conf import settings
import os
from typing import Iterable
from .sample import Sample


class SampleFileManager(models.Manager):
    
    def add_file(self, file_info:dict):
        file_obj = self.create(**file_info)
        file_obj.exist = file_obj.file_exists()
        file_obj.save()
        return file_obj
    
    def get_sample_files(self, batch_name:str, sample_name:str):
        '''
        one sample may include 0-many files
        '''
        sample = Sample.objects.filter(batch_name=batch_name, sample_name=sample_name)
        if sample:
            return self.model.objects.filter(sample=sample[0])
        return []

    def iterate_batch_files(self, batch_name:str, file_type:str=None, \
            file_format:str=None)->Iterable:
        '''
        Iteration of all files given a batch name
        '''
        cond = {}
        if file_type is not None:
            cond['file_type'] = file_type
        if file_format is not None:
            cond['file_format'] = file_format
        samples = Sample.objects.filter(batch_name=batch_name)
        for sample in samples:
            cond['sample'] = sample
            sample_files = self.filter(**cond)
            for file_obj in sample_files:
                yield sample.sample_name, file_obj
                 
    def get_batch_files(self, batch_name:str, file_type:str=None):
        batch = {} 
        batch_files = self.iterate_batch_files(batch_name, file_type)
        for sample_name, file_obj in batch_files:
            s = {
                'file_path': file_obj.file_path,
                'is_file': file_obj.file_exists(),
            }
            if sample_name in batch:
                batch[sample_name].append(s)
            else:
                batch[sample_name] = [s,]
        return batch

    def check_not_found_files(self, batch_name:str):
        batch = {} 
        batch_files = self.iterate_batch_files(batch_name)
        for sample_name, file_obj in batch_files:
            if file_obj.file_exists:
                if sample_name in batch:
                    batch[sample_name].append(file_obj.file_path)
                else:
                    batch[sample_name] = [file_obj.file_path,]
        return batch




class SampleFile(models.Model):
    # one sample may include multiple files
    sample = models.ForeignKey(Sample,
        on_delete = models.CASCADE
    )
    # relative path
    file_name = models.CharField(max_length = 1256)
    # namely fastq and so on
    file_format = models.CharField(max_length=24, blank=True)
    # namely R1/R2...
    file_type = models.CharField(max_length=24, blank=True)
    # duplicates
    batch_no = models.CharField(max_length = 128,
        blank=True, null=True
    )
    exist = models.BooleanField(default=False)

    objects = SampleFileManager()

    class Meta:
        app_label = 'sample'
        ordering = ('sample', 'file_name')

    @property
    def storage_path(self):
        return settings.DATA_DIR

    @property
    def file_path(self):
        return os.path.join(self.storage_path, self.file_format, \
            self.file_type, self.file_name)

    def file_exists(self)->bool:
        if os.path.isfile(self.file_path):
            return True
        return False