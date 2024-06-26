from django.contrib import admin
from .models import Categoria, Produto, Cliente, Fornecedor, Compra, CompraProdutoItem, Venda, VendaProdutoItem

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Compra)
admin.site.register(CompraProdutoItem)
admin.site.register(Venda)
admin.site.register(VendaProdutoItem)