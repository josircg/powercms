from django.conf import settings
from django.core.management.base import BaseCommand

from django.contrib.admin.models import LogEntry
from cms.models import URLNotFound


class Command(BaseCommand):
    help = 'Wipe Log and URLs not found'

    def handle(self, *args, **options):
        LogEntry.objects.all().delete()
        URLNotFound.objects.all().delete()
        print('Logs removidos')


