from django import forms
from app_1.models import Contact, NewsLetter

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email', 'subject', 'message']

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'