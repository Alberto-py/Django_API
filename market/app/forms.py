from django import forms
from . import models, validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))

    class Meta:
        model = models.Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    #Validaciones en el Formulario Agregar Producto
    """nombre = forms.CharField(min_length=4, max_length=50)
    imagen = forms.ImageField(required=False)
    precio = forms.IntegerField(min_value=1, max_value=1000000)"""

    imagen = forms.ImageField(validators = [validators.MaxSizeFileValidator(max_file_size=2)])

    """def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = models.Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre de producto ya existe")
        
        return nombre"""

    class Meta:
        model = models.Producto
        fields = '__all__'

        widgets ={
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]