# -*- coding: utf-8 -*-
 
from django.forms import ModelForm
from models import Order, OrderServices
from django.conf import settings
from livesettings import config_value
from django.core.mail import send_mail
from django.template import Context, Template


def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        [config_value('MyApp', 'EMAIL')])

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('date', )
    
      
    def save(self, *args, **kwargs):
        super(OrderForm, self).save(*args, **kwargs)
        subject=u'Поступил новый заказ',
        
        body_templ="""
{% for field in form %}
    {% if field.name != 'services' %}{{ field.label }} - {{ field.value }}{% endif %}
{% endfor %}

Дополнительные услуги:
{% for s in services %}
    - {{ s }}
{% empty %}
    Отсутствуют.
{% endfor %}
            """
        ctx = Context({
            'form': self,
            'services': [OrderServices.objects.get(id=int(x)) for x in self['services'].data],
        })
        body = Template(body_templ).render(ctx)
        sendmail(subject, body)