from django.db import models


class Produto(models.Model):
    sku = models.IntegerField('SKU')
    nome = models.CharField('Nome do Produto', max_length=255)
    cor = models.CharField('Cor do Produto', max_length=255)
    tamanho = models.CharField('Tamanho', max_length=1)
    categoria = models.CharField('Categoria', max_length=255)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    SEX = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    nome = models.CharField('Nome', max_length=255)
    sobrenome = models.CharField('Sobrenome', max_length=255)
    telefone = models.CharField('Telefone', max_length=11)
    endereco = models.CharField('Endereço', max_length=255)
    cidade = models.CharField('Cidade', max_length=255)
    estado = models.CharField('Estado', max_length=255)
    cep = models.CharField('CEP', max_length=8)
    sexo = models.CharField('Sexo', max_length=1, choices=SEX)
    creditlimit = models.DecimalField('Limite de Crédito', max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Pedido(models.Model):
    datapedido = models.DateTimeField('Data do Pedido')
    datapgto = models.DateTimeField('Data do Pagamento')
    dataenvio = models.DateTimeField('Data do Envio')
    status = models.IntegerField('Status')
    fontemkt = models.CharField('Fonte de Marketing', max_length=255)
    comentarios = models.CharField('Comentários', max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)


class OrderProduto(models.Model):
    qte = models.IntegerField('Quantidade')
    precounit = models.DecimalField('Preço Unitário', max_digits=8, decimal_places=2)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, default=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, default=1)


class Pagamento(models.Model):
    datapgto = models.DateTimeField('Data do Pagamento')
    meiopgto = models.CharField('Meio de Pagamento', max_length=255)
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
