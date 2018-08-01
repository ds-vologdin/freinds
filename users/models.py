from django.db import models
from django.db.models import CharField, DateField, SlugField, TextField
from django.db.models import DateTimeField, CharField, ForeignKey
from django.db.models import ManyToManyField

from django.utils import timezone


# Примеры заполнения моделей смотрите в модулях factories и management.commands
class User(models.Model):
    username = SlugField(max_length=50, unique=True)
    name = CharField(max_length=200)
    birthday = DateField(null=True, blank=True)
    freinds = ManyToManyField('self')

    def __str__(self):
        return '{}: {}'.format(self.username, self.name)


class RequestFreind(models.Model):
    STATUS_CHOICES = (
        ('accept', 'Принят'),
        ('deny', 'Отказ'),
        ('none', 'Запрос'),
    )
    from_user = ForeignKey(
        'User', related_name='request_freinds_send', on_delete=models.CASCADE
    )
    to_user = ForeignKey(
        'User', related_name='request_freinds_recv', on_delete=models.CASCADE
    )
    message = TextField(blank=True)
    datetime_request = DateTimeField(default=timezone.now)
    datetime_accept = DateTimeField(null=True, blank=True)
    status = CharField(
        max_length=6, choices=STATUS_CHOICES, default='none'
    )

    def accept_request(self):
        self.from_user.freinds.add(self.to_user)
        self.status = 'accept'
        self.save()

    def deny_request(self):
        self.status = 'deny'
        self.save()
