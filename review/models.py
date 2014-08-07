# -*- coding: utf-8 -*-
from django.db import models
from wedding.models import Place
from pytils import dt, translit

from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, Template
from livesettings import config_value

def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        [config_value('MyApp', 'EMAIL')])

class Review(models.Model):
    name = models.CharField(u'Имена пары', max_length=255)
    place = models.CharField(u'Место проведения торжества', max_length=255)
    text = models.TextField(u'Текст отзыва')
    photo = models.ImageField(upload_to=lambda instance, filename: 'uploads/reviews/' + translit.translify(filename),
                              null=True, blank=True, max_length=256, verbose_name=u'Фотография')
    request_date = models.DateTimeField(u'Дата добавления', auto_now_add=True)
    approved = models.BooleanField(default=False, verbose_name=u'Одобрено')

    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'
        ordering = ['-request_date']

    def __unicode__(self):
        return u'%s от %s' % (self.name, dt.ru_strftime(u"%d %B %Y", self.request_date))

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        subject=u'Поступил новый отзыв',
        body_templ="""
            Имя: {{ r.name }}
            Текст: {{ r.text }}

            Одобрить отзыв Вы можете здесь: http://h2h-wedding.com/admin/review/review/
            """
        ctx = Context({
            'r': self
        })
        body = Template(body_templ).render(ctx)
        sendmail(subject, body)
