from django import forms
from .models import NewCar



class NewCarForm(forms.ModelForm):
    class Meta:
        model = NewCar
        fields = '__all__'
