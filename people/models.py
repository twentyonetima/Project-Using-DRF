from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class People(models.Model):
    title = models.CharField('Full name', max_length=255)
    content = models.TextField('Discription', blank=True)
    time_create = models.DateTimeField('Time create', auto_now_add=True)
    time_update = models.DateTimeField('Time update', auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField('Title', max_length=100, db_index=True)

    def __str__(self):
        return self.name
