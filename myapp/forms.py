from django import forms
from .models import Contact


class SearchForm(forms.Form):
    query = forms.CharField(required=False)


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
