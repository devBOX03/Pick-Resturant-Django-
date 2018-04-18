from django import forms

from .models import ResturantLocation

class ResturantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = ResturantLocation
        fields = [
            'name',
            'location',
            'category',
        ]
