from django import forms
from shorty.models import Url
from shorty.utils import url_decode

__author__ = 'cingusoft'


class Private_Form(forms.Form):
    private_password = forms.CharField(widget=forms.PasswordInput())
    cpdr_slg = forms.CharField(widget=forms.HiddenInput())
    cpdr_slg_d = forms.CharField(widget=forms.HiddenInput())
    
    def clean(self):
        cleaned_data = super(Private_Form,self).clean()
        slug = cleaned_data.get("cpdr_slg")
        type_slug = cleaned_data.get("cpdr_slg_d")
        p_password = cleaned_data.get("private_password")
        if type_slug == "1":
            
            try:
                url = Url.objects.get(personal_slug=slug)
            except Url.DoesNotExist:
                raise forms.ValidationError("Ops, something goes wrong ")
        
        else:
            
            try:
                url = Url.objects.get(id=url_decode(slug))
            except Url.DoesNotExist:
                raise forms.ValidationError("Ops, something goes wrong ")
            
        if p_password != url.private_password:
            raise forms.ValidationError("Wrong Password ")
        
        return cleaned_data
            
class Shorty_Form(forms.Form):
    link_url = forms.URLField()
    personal_slug = forms.CharField(max_length=20,required=False)
    private_password = forms.CharField(widget=forms.PasswordInput(),required=False)