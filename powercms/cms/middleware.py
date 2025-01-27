from .views import URLMigrateView
from django.http import Http404
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


# pode morrer
class URLMigrateFallbackMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response # No need to check for a URLMigrateView for non-404 responses.
        try:
            return URLMigrateView().get(request, old_url=request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
