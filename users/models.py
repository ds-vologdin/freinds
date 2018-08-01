from django.db import models
from django.db.models import CharField, DateField, SlugField
from django.db.models import ManyToManyField


# Примеры заполнения моделей смотрите в модулях factories и management.commands
class User(models.Model):
    username = SlugField(max_length=50, unique=True)
    name = CharField(max_length=200)
    birthday = DateField(null=True, blank=True)
    freinds = ManyToManyField('self')

    def get_all_freinds(self):
        user_freinds = list(
            User.freinds.through.objects.filter(
                to_user_id__exact=self.id
            ).all()
        )
        user_freinds_id = []
        for user_freind in user_freinds:
            user_freinds_id.append(user_freind.from_user_id)

        friends = list(User.objects.filter(id__in=user_freinds_id).all())
        friends += self.freinds.all()
        return friends

    def __str__(self):
        return '{}: {}'.format(self.username, self.name)
