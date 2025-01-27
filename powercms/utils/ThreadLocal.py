"""
    threadlocals middleware
    ~~~~~~~~~~~~~~~~~~~~~~~

    make the request object everywhere available (e.g. in model instance).

    based on: http://code.djangoproject.com/wiki/CookBookThreadlocalsAndUser

    Put this into your settings:
    --------------------------------------------------------------------------
        MIDDLEWARE_CLASSES = (
            ...
            'util.ThreadLocal.ThreadLocalMiddleware',
            ...
        )
    --------------------------------------------------------------------------


    Usage:
    --------------------------------------------------------------------------
    from util import ThreadLocal

    # Get the current request object:
    request = ThreadLocal.get_current_request()

    # You can get the current user directy with:
    user = ThreadLocal.get_current_user()
    --------------------------------------------------------------------------

    :copyleft: 2009-2011 by the django-tools team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from django.utils.deprecation import MiddlewareMixin
from threading import local


_thread_locals = local()


def get_current_request():
    """ returns the request object for this thead """
    return getattr(_thread_locals, "request", None)


def get_current_user():
    """ returns the current user, if exist, otherwise returns None """
    request = get_current_request()
    if request:
        return getattr(request, "user", None)


class ThreadLocalMiddleware(MiddlewareMixin):

    """ Simple middleware that adds the request object in thread local storage."""
    def process_request(self, request):
        _thread_locals.request = request