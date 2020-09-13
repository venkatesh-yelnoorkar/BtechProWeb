from django import forms

class TitleForm(forms.Form):
    title = forms.CharField(max_length=10000, )

class AbstractForm(forms.Form):
    abstract = forms.CharField(max_length=10000, )

