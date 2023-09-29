import json
from django.db import models
from commons.models import CustomUser

class SampleManager(models.Manager):

    def batch_exists(self, batch_name:str)->bool:
        batch = self.filter(batch_name=batch_name)
        if len(batch) == 0:
            return False
        return True

    def sample_exists(self, batch_name:str, sample_name:str)->bool:
        sample = self.filter(batch_name=batch_name, sample_name=sample_name)
        if len(sample) == 0:
            return False
        return True

    def get_sample_names_by_batch(self, batch_name:str)->list:
        '''
        return sample names given batch_name
        '''
        samples = self.filter(batch_name=batch_name)
        return [s.sample_name for s in samples]

    def get_sample_names_by_user(self, user_name:str)->dict:
        '''
        given a user, return all batches with sample names created by the user
        '''
        batches = {}
        user = CustomUser.objects.get(user_name=user_name)
        samples = self.model.objects.filter(creator=user)
        for sample in samples:
            batch_name = sample.batch_name
            sample_name = sample.sample_name
            if batch_name in batches:
                batches[batch_name].append(sample_name)
            else:
                batches[batch_name] = [sample_name,]
        return batches

    def get_batch_names(self)->set:
        '''
        return all batch names
        '''
        names = [i.batch_name for i in self.all()]
        return set(names)
    
    def load_samples(self, user_name:str, samples:list):
        '''
        import samples into database
        '''
        n = 0
        user = CustomUser.objects.get_user_by_user_name(user_name)
        for sample in samples:
            sample_obj = self.create(batch_name = sample['batch_name'], \
                sample_name=sample['sample_name'], creator=user)
            if 'metadata' in sample:
                sample_obj.metadata = json.dumps(sample['metadata'])
            sample_obj.save()
            n += 1
        return n
    

    def update_sample_name(self, batch_name:str, old_name:str, new_name:str):
        '''
        update sample name and keep unique
        '''
        sample = self.filter(batch_name=batch_name, sample_name=old_name)
        if len(sample) == 1:
            new_sample = self.model.objects.filter(
                batch_name=batch_name, sample_name=new_name)
            if len(new_sample) == 0:
                sample.update(sample_name=new_name)
                return self.get(batch_name=batch_name, sample_name=new_name)
        # elif len(sample) == 0:
        #     raise ValueError("The sample is not existing. " + \
        #         f"batch_name={batch_name}, sample_name={old_name}")
        return None

    def delete_sample(self, batch_name:str, sample_name:str):
        return self.filter(batch_name=batch_name, sample_name=sample_name).delete()

    def delete_batch_samples(self, batch_name:str):
        return self.model.objects.filter(batch_name=batch_name).delete()

    def export_batch(self, batch_name:str)->dict:
        '''
        export table to nested dict
        '''
        batch = {}
        samples = self.filter(batch_name=batch_name)
        for sample in samples:
            batch[sample.sample_name]=vars(sample)
        return batch



class Sample(models.Model):
    # one batch include many samples
    batch_name = models.CharField(max_length=50)
    # one sample on one name
    sample_name = models.CharField(max_length=100)
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    # namely phenotype
    # string type converted from json format
    metadata = models.CharField(max_length=3000, \
        blank=True, null=True)

    objects = SampleManager()
    unique_together = ('batch_name', 'sample_name')

    class Meta:
        app_label = 'sample'
        ordering = ('batch_name', 'sample_name')

    def __str__(self):
        return f"{self.batch_name}_{self.sample_name}"



