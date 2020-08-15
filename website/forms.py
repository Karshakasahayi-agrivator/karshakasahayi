from django import forms

class orderform(forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    phone=forms.CharField(label='phone', max_length=11)
    email = forms.EmailField(label='Email', max_length=100)
    address=forms.CharField(label='address')
    workers=forms.IntegerField(label='workers',max_value=50)
    date_required=forms.DateField(label="Required_date")