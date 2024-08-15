from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)