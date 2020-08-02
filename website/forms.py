from django import forms

class orderform(forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    phone=forms.CharField(label='phone', max_length=11)
    address=forms.CharField(label='address')
    workers=forms.CharField(label='workers',max_length=10)
