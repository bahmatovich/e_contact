from imp import load_source
from django import template
from eflatpages.models import EFlatPage

register = template.Library()

@register.assignment_tag()
def get_eflatpages():
    return EFlatPage.objects.filter(visible=True)
