from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the first user'

    def handle(self, *args, **kwargs):
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.WARNING('User "admin" already exists.'))
        else:
            User.objects.create_user(
                username='admin',
                email='ethiobinamerplc@gmail.com',
                password='#123456'
            )
            self.stdout.write(self.style.SUCCESS('Successfully created the user "admin".'))
