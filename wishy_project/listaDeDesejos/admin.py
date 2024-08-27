from django.contrib import admin
from .models import ListaDeDesejos, Presente

class PresenteInline(admin.TabularInline):
    model = Presente
    extra = 1

@admin.register(ListaDeDesejos)
class ListaDeDesejosAdmin(admin.ModelAdmin):
    inlines = [PresenteInline]
    list_display = ('nome', 'usuario', 'data_criacao')
    search_fields = ('nome', 'usuario__username')

@admin.register(Presente)
class PresenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lista', 'preco', 'querometro')
    search_fields = ('nome', 'lista__nome')
