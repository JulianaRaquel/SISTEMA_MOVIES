from django.db import models
from django.utils.safestring import mark_safe

class Genero(models.Model):
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.genero

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Produto(models.Model):
    titulo = models.CharField(max_length=300)
    descricao = models.TextField()
    img = models.ImageField(upload_to='post_img')
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco = models.FloatField(default=0)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="media/{self.img.url}">'

    def __str__(self):
        return self.titulo

    class Meta():
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
