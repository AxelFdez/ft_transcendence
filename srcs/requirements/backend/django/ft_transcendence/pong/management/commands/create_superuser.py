from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crée un superutilisateur si il n\'existe pas'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='axel').exists():
            User.objects.create_superuser('axel', 'mon_email@example.com', '1234')
            self.stdout.write(self.style.SUCCESS('Superutilisateur créé avec succès'))
        else:
            self.stdout.write(self.style.WARNING('Le superutilisateur existe déjà'))

if __name__ == '__main__':
    Command.handle()