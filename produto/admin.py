from django.contrib import admin
from produto.models import Genero, Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('icone', 'titulo', 'genero', 'preco', 'ativo')
    list_editable = ('preco', 'ativo')

admin.site.register(Genero)