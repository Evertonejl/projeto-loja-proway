# Generated by Django 4.0.4 on 2022-07-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', '0003_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
