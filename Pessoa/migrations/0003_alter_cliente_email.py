# Generated by Django 4.0.4 on 2022-07-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', '0002_usuario_alter_fornecedor_cpfcnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]