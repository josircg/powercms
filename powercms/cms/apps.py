from django.apps import AppConfig
from django.core import checks

from .checks import check_settings, check_upload_dir


class CMSConfig(AppConfig):
    name = 'cms'
    verbose_name = 'CMS'
    verbose_name_plural = 'CMS'

    def ready(self):
        super().ready()
        checks.register(check_settings, 'powercms')
        checks.register(check_upload_dir, 'powercms')
