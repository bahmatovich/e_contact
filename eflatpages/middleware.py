from django.conf import settings
from eflatpages.views import eflatpage
from django.http import Http404


class EFlatpageFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response
        try:
            return eflatpage(request, request.path_info)
        except Http404:
            return response
        except Exception:
            if settings.DEBUG:
                raise
            return response
