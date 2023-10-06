from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        su = User.objects.create(
            email='admin@mail.com',
            is_staff=True,
            is_superuser=True,
        )

        su.set_password('12345')
        su.save()
