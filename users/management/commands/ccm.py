from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        content_manager_group = Group.objects.create(name='content_manager')
        content_manager_group.permissions.add(
            Permission.objects.get(codename='add_article'),
            Permission.objects.get(codename='change_article'),
            Permission.objects.get(codename='delete_article'),
            Permission.objects.get(codename='view_article'),
        )
        content_manager_group.save()

        content_manager = User.objects.create(
            email='content_manager@mail.com',
            is_staff=True,
        )
        content_manager.set_password('12345')
        content_manager.groups.add(content_manager_group)
        content_manager.save()
