from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Categoria')
    slug = models.SlugField(unique=True, help_text='URL amigável')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']

class Receita(models.Model):
    DIFICULDADE_CHOICES = [
        ('F', 'Fácil'),
        ('M', 'Médio'),
        ('D', 'Difícil'),
    ]

    titulo = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(unique=True, verbose_name="Slug / Atalho")
    descricao_curta = models.CharField(max_length=250, verbose_name="Resumo", help_text="Aparece na listagem inicial")
    ingredientes = models.TextField(verbose_name='Ingredientes')
    modo_preparo = models.TextField(verbose_name='Modo de Preparo')
    tempo_preparo = models.PositiveIntegerField(verbose_name='Tempo (minutos)', help_text='Tempo em minutos')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="receitas", verbose_name="Categoria")
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADE_CHOICES, default='F', verbose_name="Dificuldade")
    imagem = models.ImageField(upload_to='receitas/%Y/%m/%d/', blank=True, null=True, verbose_name="Foto da Receita")
    publicado = models.BooleanField(default=False, verbose_name="Publicado?")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ['-data_criacao']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)