from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        moderator_group = Group.objects.create(name='moderator')
        moderator_group.permissions.add(
            Permission.objects.filter(codename='moderator').first()
        )
        moderator_group.save()

        moderator = User.objects.create(
            email='moderator@mail.com',
        )
        moderator.set_password('12345')
        moderator.groups.add(moderator_group)
        moderator.save()
