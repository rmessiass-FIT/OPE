# Generated by Django 3.1.7 on 2021-03-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pagamentos',
            new_name='Pagamento',
        ),
        migrations.RenameModel(
            old_name='Produtos',
            new_name='Produto',
        ),
    ]
