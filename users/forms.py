# forms.py
from django import forms

class CartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        initial_quantity = kwargs.pop('initial_quantity', 1)
        super().__init__(*args, **kwargs)
        self.fields['quantity'].initial = initial_quantity
