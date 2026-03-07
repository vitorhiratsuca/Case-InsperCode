from django.db import models
# Create your models here.

class Partner_Category(models.Model):
    '''
    Modelo das Categorias de Parceiros:
    Apenas o Titulo da Categoria para Filtros
    '''
    title = models.CharField(max_length=200)

    class Meta:

        verbose_name_plural = 'Categorias dos Parceiros'

    def __str__(self):
        return self.title

class Team_Member(models.Model):
    '''
    Modelo dos membros da equipe:null=True
    Nome, Url da foto, biografia
    '''
    name = models.CharField(max_length=200)
    photo_url = models.ImageField()
    biography = models.TextField(max_length=200)

    class Meta:

        verbose_name_plural = 'Membros do Time'

    def __str__(self):
        return self.title

class Partner(models.Model):
    '''
    Modelo de Parceiros:
    Logo, Nome, Descrição, Categoria, Contato
    '''
    logo_url = models.ImageField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    projects = models.TextField(null=True)
    category = models.ForeignKey(Partner_Category, on_delete=models.PROTECT, null=True)
    contato = models.CharField(max_length=20)

    class Meta:

        verbose_name_plural = 'Parceiros'

    def __str__(self):
        return self.title

class Activity(models.Model):
    '''
    Modelo as atividades da pagina de atividades:
    Titulo, Descrição e um coiso para os parceiros que disponibilizam essa atividade
    '''
    title = models.CharField(max_length=200)
    description = models.TextField()
    responsible_partner = models.ForeignKey(Partner, on_delete=models.PROTECT, null=True)

    class Meta:

        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.title

class Media(models.Model):
    '''
    Modelo para as Notícias :
    Titulo, Descrição e um coiso para os parceiros que disponibilizam essa atividade
    '''
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()

    class Meta:

        verbose_name_plural = 'Notícias'

    def __str__(self):
        return self.title