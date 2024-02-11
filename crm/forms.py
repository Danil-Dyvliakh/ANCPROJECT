from django import forms

class PeopleForm(forms.Form):
    order_name = forms.CharField(max_length=200, label='ПІБ')
    order_position = forms.CharField(max_length=200, label='Посада')
    order_email = forms.EmailField(max_length=200, label='Email')