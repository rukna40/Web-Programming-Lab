# carsapp/forms.py
from django import forms

class CarForm(forms.Form):
    manufacturers = [
        ('maruti_suzuki', 'Maruti Suzuki'),
        ('tata', 'Tata'),
        ('mahindra', 'Mahindra'),
        ('hyundai', 'Hyundai'),
        ('nissan', 'Nissan'),
        ('kia', 'Kia'),
        ('toyota', 'Toyota'),
        ('honda', 'Honda'),
    ]
    
    manufacturer = forms.ChoiceField(choices=manufacturers,label="Select Manufacturer")
    model = forms.CharField(max_length=100, label="Model Name")
