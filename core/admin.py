from django.contrib import admin

from .models import Categoria, Produto, Cliente, Pagamento, Pedido, OrderProduto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'creditlimit')


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pagamento)
admin.site.register(Pedido)
admin.site.register(OrderProduto)
