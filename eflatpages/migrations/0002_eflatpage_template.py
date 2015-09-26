# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eflatpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eflatpage',
            name='template',
            field=models.CharField(default=b'', help_text='\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430 \u0448\u0430\u0431\u043b\u043e\u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', max_length=100, verbose_name='\u0428\u0430\u0431\u043b\u043e\u043d', blank=True),
        ),
    ]
