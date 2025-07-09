from django.contrib import admin

# Register your models here.
from .models import Producto

registrer_models = [Producto]

admin.site.register(registrer_models)