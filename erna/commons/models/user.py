from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, is_staff=None, is_superuser=None):
        if is_staff is None:
            is_staff = False
        if is_superuser is None:
            is_superuser = False

        if not email:
            raise ValueError('wrong email')
        if not password:
            raise ValueError('wrong password')
        user_obj = self.model(
            email=self.normalize_email(email),
            is_staff = is_staff,
            is_superuser=is_superuser
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj
    
    def create_staff(self, email, password):
        return self.create_user(email, password, True)

    def create_superuser(self, email, password):
        return self.create_user(email, password, True, True)

    def get_user_by_user_name(self, user_name):
        return self.model.objects.get(user_name=user_name)

class User(AbstractBaseUser):
    # email is user name field
    email = models.EmailField(max_length=100, unique=True)
    user_name = models.CharField(max_length=256, unique=True)
    full_name = models.CharField(max_length=256, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        app_label = 'rna_seq'
        ordering = ['email']

    def __str__(self):
        return self.email
    
    @property
    def full_name(self):
        return self.full_name
    
    