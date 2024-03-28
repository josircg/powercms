import os
import re
import urllib
import requests

from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from cms.models import Theme


class Command(BaseCommand):
    help = 'Cria Tema se este não existe ainda'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--theme', type=str, help='Theme Slug')
        parser.add_argument('-p', '--path', type=str, help='Full Path')

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.abspath(__file__)).split('/')[:-3]
        theme_slug = options['theme']
        full_path = options['path']
        try:
            Theme.objects.get(path_name=theme_slug)
        except Theme.DoesNotExist:
            theme = Theme(path_name=theme_slug, active=True, path=full_path)
            theme.save()