from django import forms
from app_1.models import Contact


class NameForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email', 'subject', 'message']