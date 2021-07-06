from django.db import models

# Create your models here.
class Filme(models.Model):

    titulo = models.CharField(max_length=255, blank=False)
    duracao = models.CharField(max_length=50)
    descricao = models.TextField()
    lancamento = models.IntegerField()
    capa = models.ImageField(upload_to='images/', blank=True)   
    categoria = models.ForeignKey("Categoria",  on_delete=models.CASCADE)
    produtora = models.ForeignKey("Produtora", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo;
    def save(self):
        if self.capa == "":
            self.capa = 'images/filmeDefault.jpg'
        super(Filme, self).save()
    class Meta:
        verbose_name_plural = "Filmes"


class Categoria(models.Model):

    CATEGORIA_CHOICES = (
            ('Ação','Ação'),
            ('Animação','Animação'),
            ('Aventura','Aventura'),
            ('Comédia','Comédia'),
            ('Drama','Drama'),
            ('Documentário','Documentário'),
            ('Fantasia','Fantasia'),
            ('Ficção','Ficção científica'),
            ('Horror','Horror'),
            ('Musical','Musical'),
            ('Romance','Romance'),
            ('Suspense','Suspense'),
            ('Terror','Terror'),
            ('Outro','Outro'),
    ) 
    genero = models.CharField(max_length=255, choices=CATEGORIA_CHOICES)
    
    def __str__(self):
        return self.genero;

class Produtora(models.Model):

    PRODUTORA_CHOICES = (
        ('Fox','21st Century Fox'),
        ('DreamWorks','DreamWorks'),
        ('MGM','MGM (Metro Goldwyn Mayer)'),
        ('The Weinstein Company','The Weinstein Company'),
        ('LionsGate','Lions Gate Entertainment'),
        ('Paramount','Paramount Motion Pictures Group'),
        ('Universal','Universal Pictures'),
        ('Disney','The Walt Disney Company'),
        ('Warner','Time Warner'),
        ('Sony','Sony Pictures Entertainment'),
        ('Outro','Outro'),
    )
    nome = models.CharField(max_length=255, choices=PRODUTORA_CHOICES)
    def __str__(self):
        return self.nome;
