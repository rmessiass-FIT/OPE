from django.db import models


class Categoria(models.Model):
    CAT = (
        (1, 'Bermuda'),
        (2, 'Calça'),
        (3, 'Camiseta'),
        (4, 'Blusa'),
        (5, 'Saia'),
        (6, 'Vestido')
    )
    categoria = models.IntegerField('Categoria', choices=CAT)


class Produto(models.Model):
    TAMANHO = (
        (1, 'P'),
        (2, 'M'),
        (3, 'G'),
        (4, 'GG'),
        (5, 'XG')
    )
    sku = models.CharField('SKU', max_length=10)
    nome = models.CharField('Nome do Produto', max_length=50)
    cor = models.CharField('Cor do Produto', max_length=10)
    tamanho = models.IntegerField('Tamanho', choices=TAMANHO)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    SEX = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    UF = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AM', 'Amazonas'),
        ('AP', 'Amapá')
    )
    nome = models.CharField('Nome', max_length=50)
    telefone = models.CharField('Telefone', max_length=11)
    endereco = models.CharField('Endereço', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=2, choices=UF)
    cep = models.CharField('CEP', max_length=8)
    sexo = models.CharField('Sexo', max_length=1, choices=SEX)
    creditlimit = models.DecimalField('Limite de Crédito', max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.nome}'


class Pagamento(models.Model):
    FORMA_PGTO = (
        (1, 'Cartão de Crédito'),
        (2, 'Boleto'),
        (3, 'Pix'),
        (4, 'Transferência Bancária')
    )
    datapgto = models.DateTimeField('Data do Pagamento')
    meiopgto = models.IntegerField('Meio de Pagamento', choices=FORMA_PGTO)
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)


class Pedido(models.Model):
    STATUS_PEDIDO = (
        (1, 'Aguardando Pagamento'),
        (2, 'Em processamento'),
        (3, 'Enviado'),
        (4, 'Não Entregue'),
        (5, 'Entregue'),
        (6, 'Devolvido')
    )
    FONTE_MKT = (
        (1, 'Instagram'),
        (2, 'Facebook'),
        (3, 'Agência de Mkt')
    )
    datapedido = models.DateField('Data do Pedido')
    dataenvio = models.DateField('Data do Envio')
    status = models.IntegerField('Status', choices=STATUS_PEDIDO)
    fontemkt = models.IntegerField('Fonte de Marketing', choices=FONTE_MKT)
    comentarios = models.CharField('Comentários', max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE, default=1)


class OrderProduto(models.Model):
    qte = models.IntegerField('Quantidade')
    precounit = models.DecimalField('Preço Unitário', max_digits=8, decimal_places=2)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, default=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, default=1)
