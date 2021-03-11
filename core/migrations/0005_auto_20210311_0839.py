# Generated by Django 3.1.7 on 2021-03-11 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210310_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduto',
            name='pedido_id',
        ),
        migrations.RemoveField(
            model_name='orderproduto',
            name='sku',
        ),
        migrations.RemoveField(
            model_name='pagamento',
            name='cliente_id',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cliente_id',
        ),
        migrations.AddField(
            model_name='orderproduto',
            name='pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.pedido'),
        ),
        migrations.AddField(
            model_name='orderproduto',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.produto'),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.cliente'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1, verbose_name='Sexo'),
        ),
    ]