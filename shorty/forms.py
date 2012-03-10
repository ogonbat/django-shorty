from django import forms
from shorty.models import Pslug

__author__ = 'ogonbat'


class Private_Form(forms.Form):
    private_password = forms.CharField(widget=forms.PasswordInput())

class Shorty_Form(forms.Form):
    link_url = forms.URLField()
    personal_slug = forms.CharField(max_length=20,required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        try:
            slug_unique = Pslug.objects.get(slug__exact=cleaned_data['personal_slug'])
        except Pslug.DoesNotExist:
            return cleaned_data
        raise forms.ValidationError("The personal Slug already exist")