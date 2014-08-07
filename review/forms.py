# -*- coding: utf-8 -*-

from django.forms import ModelForm
from review.models import Review
from wedding.models import Place

import autocomplete_light

class PlaceAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name']

autocomplete_light.register(Place, PlaceAutocomplete)

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('request_date', 'approved', )

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['size'] = 48
        self.fields['name'].widget.attrs['placeholder'] = u'Например, Иван и Мария'
        self.fields['place'].widget = autocomplete_light.TextWidget('PlaceAutocomplete')
        self.fields['place'].widget.attrs['size'] = 48

    def save(self, *args, **kwargs):
        super(ReviewForm, self).save(*args, **kwargs)
