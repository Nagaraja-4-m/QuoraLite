from django.db import models
from helper.models import DateTimeModelMixin
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class UserAccount(AbstractBaseUser,PermissionsMixin, DateTimeModelMixin):
    # Django user fields
    groups              =   None
    user_permissions    =   None
    is_staff            =   models.BooleanField(default=False)

    id                  =  models.AutoField(primary_key=True)
    # Personal info
    first_name      =   models.CharField(max_length=16)
    last_name       =   models.CharField(max_length=16, null=True)
    email           =   models.EmailField(max_length=255,unique=True)
    password        =   models.CharField(max_length=1024,editable=False)

    USERNAME_FIELD      =   'email'
    REQUIRED_FIELDS     =   ['first_name','last_name']
    objects             =   CustomUserManager()


    def __str__(self) -> str:
        return self.first_name + " " +self.last_name if self.last_name else self.first_name
