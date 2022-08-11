from .models import Producto, Marca
from rest_framework import serializers
from .forms import CustomUserCreationForm

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):

    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marca")
    nombre = serializers.CharField(required=True, min_length=4)

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()

        """if existe:
            raise serializers.ValidationError("Este nombre de producto ya existe")

        return value"""

    class Meta:
        model = Producto
        fields = '__all__'
        # Para excluir algun campo
        # exclude = ['nombre']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserCreationForm
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance