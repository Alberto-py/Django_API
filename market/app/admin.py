from django.contrib import admin
from .models import Marca, Producto, Contacto
from .forms import ProductoForm

class Produc_Admin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["nuevo", "marca"]
    list_per_page = 5
    #Validator en el Admin
    form = ProductoForm

admin.site.register(Marca)
admin.site.register(Producto, Produc_Admin)
admin.site.register(Contacto)