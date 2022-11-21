from django.db import models


class BaseModel(models.Model):
    '''abstract model base class'''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    update_time = models.DateTimeField(auto_now=True, verbose_name="Upload time")
    is_delete = models.BooleanField(default=False, verbose_name='Delete')

    class Meta:
        # abstract model class
        abstract = True
