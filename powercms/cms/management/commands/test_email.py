from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives

from cms.models import Recurso


class Command(BaseCommand):
    help = 'Teste de Envio de Email'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--to', type=str, help='Destinatário')

    def handle(self, *args, **options):
        try:
            a = Recurso.objects.get(id=1)
        except Recurso.DoesNotExist:
            pass
        destino = [ options['to'] ]
        headers = {'Reply-To': settings.REPLY_TO_EMAIL, }
        msg = EmailMultiAlternatives('Teste', 'TESTE', settings.DEFAULT_FROM_EMAIL, to=destino,
                                     headers=headers)
        msg.attach_alternative('TESTE', mimetype='text/html; charset=UTF-8')
        msg.send()
        print('Email enviado com sucesso!')


