from django.db import models
import os

STANDER_FORMAT = {
  'FQ': 'FSTQ',
  'FASTQ': 'FASTQ',
  'FA': 'FASTA',
  'FASTA': 'FASTA',
  'SAM': 'SAM',
  'BAM': 'BAM',
  'GBK': 'GBK',
  'GTF': 'GTF',
  'GFF': 'GFF',
  'GFF3': 'GFF3',
}

class RawDataManager(models.Manager):
  def get_batch_files(self, batch_name:str):
    return self.filter(batch_name=batch_name)

  def detect_file_format(self, file_name:str):
    split_tup = os.path.splittext(file_name)
    file_type = split_tup[1].toupper() if len(split_tup) > 1 else None
    return STANDER_FORMAT.get(file_type, "UN")

  def add_data(self, batch_name:str, full_file_path:str):
    file_path = os.file.dirname(full_file_path)
    file_name = os.file.basename(full_file_path)
    file_type = self.detect_file_format(file_name)
    self.create(batch_name=batch_name, file_path=file_path, \
      file_name=file_name, file_type=file_type)

class RawData(models.Model):
  batch_name = models.CharField(max_length=20)
  file_path = models.CharField(max_length=512)
  file_name = models.CharField(max_length=128)
  file_type = models.CharField(
    max_length=10,
    blank=True,
    null=True
  )

  objects = RawDataManager()

  class Meta:
    app_label = 'sample'
    ordering = ['batch_name', 'file_path']
