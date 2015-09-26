# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EFlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(help_text='\u0412\u0435\u0434\u0438\u0442\u0435 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 url', unique=True, max_length=100, verbose_name='URL')),
                ('title', models.CharField(help_text='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', max_length=100, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', models.CharField(default='', help_text='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0442\u0435\u0433\u0430 description', max_length=200, verbose_name='Description', blank=True)),
                ('keywords', models.CharField(default='', help_text='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0442\u0435\u0433\u0430 keywords', max_length=200, verbose_name='Keywords', blank=True)),
                ('visible', models.BooleanField(default=True, help_text='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u043d\u0430 \u0441\u0430\u0439\u0442\u0435', verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('order', models.PositiveIntegerField(default=0, help_text='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e', verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('body', models.TextField(default=b'', help_text='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0432 html', verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435', blank=True)),
            ],
        ),
    ]
