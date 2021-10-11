from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# from django import forms
#
# class Registration(forms.Form):
#     choice = forms.ChoiceField(required=True)


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, please, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            WHERE=self.please,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, please, password):
        user = self.create_user(
            email,
            password=password,
            WHERE = please,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    region = ('동구', '서구', '남구', '북구', '광산구')
    please = models.CharField(max_length=30, blank=False, null=False, choices=region)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['please']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin