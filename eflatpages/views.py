from django.conf import settings
from eflatpages.models import EFlatPage
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

DEFAULT_TEMPLATE = 'eflatpages/default.html'

def eflatpage(request, url):
    if not url.startswith('/'):
        url = '/' + url
    try:
        f = get_object_or_404(
            EFlatPage,
            url=url,
            visible=True
        )
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            f = get_object_or_404(
                EFlatPage,
                url=url,
                visible=True
            )
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    return render_eflatpage(request, f)


@csrf_protect
def render_eflatpage(request, f):
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    if f.template:
        template = loader.select_template((f.template, DEFAULT_TEMPLATE))
    else:
        template = loader.get_template(DEFAULT_TEMPLATE)

    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    response = HttpResponse(template.render({'eflatpage': f}, request))
    return response
