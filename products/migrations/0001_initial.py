# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('photo', models.ImageField(upload_to=b'product-classes', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('visible', models.BooleanField(default=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u0441\u0430\u0439\u0442\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u043b\u0430\u0441\u0441 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432',
                'verbose_name_plural': '\u041a\u043b\u0430\u0441\u0441\u044b \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432',
            },
        ),
    ]
