# Generated by Django 4.0.4 on 2022-05-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50, unique=True)),
                ('senha', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Usuario',
            },
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cpfcnpj',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
