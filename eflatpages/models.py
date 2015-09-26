# -*- coding: utf-8 -*-
from django.db import models

class EFlatPage(models.Model):
    url = models.CharField(
        max_length=100,
        verbose_name=u'URL',
        help_text=u'Ведите относительный url',
        unique=True,
    )

    title = models.CharField(
        max_length=100,
        verbose_name=u'Заголовок',
        help_text=u'Заголовок страницы'
    )

    description = models.CharField(
        max_length=200,
        default=u'',
        blank=True,
        verbose_name=u'Description',
        help_text=u'Введите значение тега description'
    )

    keywords = models.CharField(
        max_length=200,
        default=u'',
        blank=True,
        verbose_name=u'Keywords',
        help_text=u'Введите значение тега keywords'
    )

    visible = models.BooleanField(
        default=True,
        verbose_name=u'Отображение',
        help_text=u'Отображать страницу на сайте'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name=u'Сортировка',
        help_text=u'Значение сортировки по возрастанию'
    )

    registration_required = models.BooleanField(
        default=False,
        verbose_name=u'Требовать регистрацию',
        help_text=u'Данная страница будет доступна только зарегестрированным пользователям'
    )

    content = models.TextField(
        default='',
        blank=True,
        verbose_name=u'Содержимое',
        help_text=u'Введите содержимое страницы в html'
    )

    template = models.CharField(
        default='',
        blank=True,
        max_length=100,
        verbose_name=u'Шаблон',
        help_text=u'Имя файла шаблона страницы'
    )

    def __unicode__(self):
        return u'%s - %s' % (self.url, self.title)

    def __str__(self):
        return str(self.__unicode__())

    class Meta:
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'
        ordering = ['order']
