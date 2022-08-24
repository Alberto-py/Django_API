from django import forms
from . import models

class ContactoForm(forms.ModelForm):
    
    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))

    class Meta:
        model = models.Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'