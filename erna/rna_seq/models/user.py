from django.db import models

# Create your models here.


class UserModel(models.Model):
    USER_STATUS = [
        ('A','active'),
        ('R','revoke'),
        ('I','inactive'),
    ]
    user_id = models.CharField(primary_key=True, max_length=10)
    user_name = models.CharField(max_length=50, unique=True,
        verbose_name='name of user')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=USER_STATUS, max_length=10)

    class Meta:
        app_label = 'rna_seq'
        ordering = ('user_id',)
    
    def __str__(self):
        return self.user_name
    