from django.core.management.base import BaseCommand
from users.factories import UserFactory


class Command(BaseCommand):
    help = 'Создание фейковых пользователей'

    def add_arguments(self, parser):
        parser.add_argument('size_batch', type=int, default=5)

    def handle(self, *args, **options):
        users = UserFactory.create_batch(options['size_batch'])

        self.stdout.write(self.style.SUCCESS('Создали {} записей'.format(
            options['size_batch']
        )))
        for user in users:
            self.stdout.write(self.style.SUCCESS(
                '{0.username} - {0.name}'.format(user)
            ))
