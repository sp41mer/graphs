# coding=utf-8
from __future__ import unicode_literals
from django.db import models



class Student(models.Model):
    Botan, Good, Prepod, Dva, Missers = u'Отличники', u'Хорошисты', u'Преподаватели', u'Двоечники', u'Прогульщики'
    CHOICES = ((0, Botan), (1, Good),
               (2, Prepod), (3, Dva), (4, Missers))

    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self', verbose_name=u'Друзья', related_name='friends', blank=True)
    group = models.IntegerField(choices=CHOICES, verbose_name=u'Группа')

    def __str__(self):
        return u'{}'.format(self.name)

