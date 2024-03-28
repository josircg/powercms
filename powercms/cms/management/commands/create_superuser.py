from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from cms.models import Recurso

class Command(BaseCommand):
    help = 'Cria Admin User e atribui o nome do serviço no supervisor'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--service', type=str, help='service slug')
        parser.add_argument('-p', '--password', type=str, help='password')

    def handle(self, *args, **options):
        pwd = options['password']
        slug = options['service']
        if pwd:
            try:
                User.objects.get(username='admin')
            except User.DoesNotExist:
                user = User.objects.create_user(username='admin', email='', password=pwd)
                user.is_staff = True
                user.is_superuser = True
                user.save()

        if slug:
            Recurso.objects.get_or_create(recurso='SUP_SLUG', defaults={'valor': slug, 'ativo': True})