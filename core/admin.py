from django.contrib import admin

from .models import Produto, OrderProduto, Pedido, Cliente, Pagamento


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'creditlimit')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(OrderProduto)
admin.site.register(Pedido)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pagamento)
