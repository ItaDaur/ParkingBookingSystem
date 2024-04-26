from django import forms
from .models import ParkingSlot

class CreateParkingSlotForm(forms.ModelForm):
    class Meta:
        model = ParkingSlot
        fields = ['title', 'description']

class UpdateParkingSlotForm(forms.ModelForm):
    class Meta:
        model = ParkingSlot
        fields = ['title', 'description']