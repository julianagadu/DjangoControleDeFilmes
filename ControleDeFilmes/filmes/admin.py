from django.contrib import admin
from .models import Filme, Categoria, Produtora

# Register your models here.
admin.site.register(Filme)
admin.site.register(Categoria)
admin.site.register(Produtora)