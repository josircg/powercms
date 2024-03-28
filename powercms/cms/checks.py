from django.conf import settings, global_settings
from django.core.checks import Warning, Error
from django.core.files.storage import get_storage_class
from django.utils.translation import ugettext_lazy as _


def check_settings(app_configs, **kwargs):
    errors = []
    server_email = getattr(settings, 'SERVER_EMAIL', None)

    if not server_email or global_settings.SERVER_EMAIL == server_email:
        errors.append(
            Warning(
                _('SERVER_EMAIL setting not defined or is the same as the default configuration'),
                hint=_('You must set SERVER_EMAIL on your local settings file'),
                id='powercms.W0001'
            )
        )

    admins = getattr(settings, 'ADMINS', [])

    if not admins:
        errors.append(
            Warning(
                _('ADMINS setting not defined'),
                hint=_('You must provide a list of admins emails. Ex: [("admin", "admin@email.com")]'),
                id='powercms.W0002'
            )
        )

    return errors


def check_upload_dir(app_configs, **kwargs):
    errors = []

    fs = get_storage_class()()
    upload_dir = settings.CKEDITOR_UPLOAD_PATH

    if upload_dir.endswith('/'):
        upload_dir = upload_dir[:-1]

    if not fs.exists(upload_dir):
        errors.append(
            Error(
                _('"%s" does not exist in your media directory (%s)') % (upload_dir, fs.location),
                hint=_('Add the "%s" directory into %s') % (upload_dir, fs.location),
                id='powercms.E0001'
            )
        )

    return errors
