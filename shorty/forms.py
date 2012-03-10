from django import forms

__author__ = 'ogonbat'


class Private_Form(forms.Form):
    private_password = forms.CharField(widget=forms.PasswordInput())

class Shorty_Form(forms.Form):
    link_url = forms.URLField()
    personal_slug = forms.CharField(max_length=20,required=False)
    private_password = forms.CharField(widget=forms.PasswordInput(),required=False)