# -*- coding: utf-8 -*-
from django.db import models

class ProductClass(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        null=False,
        verbose_name=u'Наименование'
    )

    photo = models.ImageField(
        upload_to='product-classes',
        blank=False,
        verbose_name=u'Изображение'
    )

    visible = models.BooleanField(
        default=True,
        verbose_name=u'Отображать на сайте'
    )

    class Meta:
        verbose_name=u'Класс продуктов'
        verbose_name_plural=u'Классы продуктов'