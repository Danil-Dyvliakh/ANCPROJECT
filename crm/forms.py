from django import forms

class PeopleForm(forms.Form):
    name = forms.CharField(max_length=200, label='ПІБ', required = False)
    position = forms.CharField(max_length=200, label='Посада')
    email = forms.EmailField(max_length=200, label='Email')