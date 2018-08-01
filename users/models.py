from django.db import models
from django.db.models import CharField, DateField, SlugField
from django.db.models import ManyToManyField


# Примеры заполнения моделей смотрите в модулях factories и management.commands
class User(models.Model):
    username = SlugField(max_length=50, unique=True)
    name = CharField(max_length=200)
    birthday = DateField(null=True, blank=True)
    freinds = ManyToManyField('self')

    def __str__(self):
        return '{}: {}'.format(self.code_name, self.name)
