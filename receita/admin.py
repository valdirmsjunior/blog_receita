from django.contrib import admin
from .models import Receita, Categoria

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'dificuldade' , 'tempo_preparo', 'publicado')
    list_filter = ('categoria', 'dificuldade', 'publicado')
    search_field = ('titulo', 'ingredientes')
    prepopulated_fields = {'slug': ('titulo',)}
    
    class Media:
        css = {
            'all': ('css/custom_admin.py',)
        }