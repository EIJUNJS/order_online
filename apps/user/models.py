from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel


class User(AbstractUser, BaseModel):
    """user model class"""

    class Meta:
        db_table = 'df_user'
        verbose_name = 'User'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    """Address model class"""
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='account')
    receiver = models.CharField(max_length=20, verbose_name='recipient')
    addr = models.CharField(max_length=256, verbose_name='Address')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='Post_code')
    phone = models.CharField(max_length=11, verbose_name='Phone')
    is_default = models.BooleanField(default=False, verbose_name='default')

    class Meta:
        db_table = 'df_address'
        verbose_name = 'address'
        verbose_name_plural = verbose_name

