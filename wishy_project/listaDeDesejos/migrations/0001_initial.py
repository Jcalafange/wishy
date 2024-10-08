# Generated by Django 5.1 on 2024-08-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListaDeDesejos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Lista')),
                ('descricao_lista', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Lista de Desejos',
                'verbose_name_plural': 'Listas de Desejos',
            },
        ),
        migrations.CreateModel(
            name='Presente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Presente')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço Médio')),
                ('querometro', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Querômetro')),
                ('descricao_presente', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('link', models.URLField(blank=True, max_length=255, null=True, verbose_name='Link para o Produto')),
            ],
            options={
                'verbose_name': 'Presente',
                'verbose_name_plural': 'Presentes',
            },
        ),
    ]
