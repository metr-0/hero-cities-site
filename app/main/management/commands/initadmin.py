from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            admin = User.objects.create_superuser(
                email='somemail@gmail.com',
                username='admin',
                password='admin'
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            raise CommandError('Admin accounts can only be initialized if no Accounts exist')
