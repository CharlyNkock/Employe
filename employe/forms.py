from django import forms
from .models import Employe


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'email', 'poste', 'salaire']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Nom'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Prénom'
            }),
            'email': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Email'
            }),
            'poste': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Poste'
            }),
            'salaire': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Salaire'
            })
        }