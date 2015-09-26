# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eflatpages', '0002_eflatpage_template'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eflatpage',
            options={'ordering': ['order'], 'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430', 'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b'},
        ),
        migrations.RenameField(
            model_name='eflatpage',
            old_name='body',
            new_name='content',
        ),
    ]
