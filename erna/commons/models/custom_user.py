from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, user_name:str, email:str, password, is_staff=None, is_superuser=None):
        if is_staff is None:
            is_staff = False
        if is_superuser is None:
            is_superuser = False

        if not email:
            raise ValueError('wrong email')
        if not password:
            raise ValueError('wrong password')
        user_obj = self.model(
            user_name = user_name,
            email=self.normalize_email(email),
            is_staff = is_staff,
            is_superuser=is_superuser
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj
    
    def create_staff(self, user_name, email, password):
        return self.create_user(user_name, email, password, True)

    def create_superuser(self, user_name, password):
        return self.create_user(user_name, password, True, True)

    def get_user_by_user_name(self, user_name):
        return self.model.objects.get(user_name=user_name)

class CustomUser(AbstractUser):
    pass


    class Meta:
        app_label = 'commons'

    def __str__(self):
        return self.username
    
    