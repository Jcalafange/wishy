from django.db import models
from django.conf import settings

class ListaDeDesejos(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome da Lista")
    descricao_lista = models.TextField(null=True, blank=True, verbose_name="Descrição")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuário")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Lista de Desejos"
        verbose_name_plural = "Listas de Desejos"

class Presente(models.Model):
    lista = models.ForeignKey(ListaDeDesejos, related_name='presentes', on_delete=models.CASCADE, verbose_name="Lista de Desejos")
    nome = models.CharField(max_length=255, verbose_name="Nome do Presente")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Médio")
    querometro = models.IntegerField(choices=[(i, i) for i in range(6)], verbose_name="Querômetro")
    descricao_presente = models.TextField(null=True, blank=True, verbose_name="Descrição")
    link = models.URLField(max_length=255, verbose_name="Link para o Produto", null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Presente"
        verbose_name_plural = "Presentes"
