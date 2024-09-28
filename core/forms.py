from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'product',
            'price',
            'shipment_value',
            'client',
            'address',
            'phone_number',
            'image',
       ]

        widgets = {
                'product': forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control'}),
                'shipment_value': forms.NumberInput(attrs={'class': 'form-control'}),
                'client': forms.TextInput(attrs={'class': 'form-control'}),
                'address': forms.TextInput(attrs={'class': 'form-control'}),
                'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
                'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }