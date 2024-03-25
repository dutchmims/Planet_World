# forms.py

from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', max_length=200)
    # Add more fields as needed (e.g., for payment details)
