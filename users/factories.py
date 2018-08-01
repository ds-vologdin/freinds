import datetime
import factory
import factory.fuzzy

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: 'user_{}'.format(n))
    name = factory.Faker('name', locale='ru_RU')
    birthday = factory.fuzzy.FuzzyDate(
        datetime.date(1970, 1, 1), datetime.date(2000, 1, 1)
    )


def create_batch_users(size=5):
    return UserFactory.create_batch(size=size)
