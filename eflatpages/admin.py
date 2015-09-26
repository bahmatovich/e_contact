# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from eflatpages.models import EFlatPage
from django_summernote.admin import SummernoteModelAdmin

class EFlatPageAdmin(SummernoteModelAdmin):
    list_display = ['url', 'title', 'visible', 'order']
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'content')
        }),
        (u'Расширенные', {
            'classes': ('collapse',),
            'fields': ('visible', 'order', 'template', 'registration_required')
        }),
        (u'Продвижение', {
            'classes': ('collapse',),
            'fields': ('description', 'keywords')
        }),
    )

admin.site.register(EFlatPage, EFlatPageAdmin)
