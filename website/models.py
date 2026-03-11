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
    
class Member_Position(models.Model):
    '''
    Modelo das posicoes dos membros:
    Apenas o Titulo e Poder
    '''
    title = models.CharField(max_length=200)
    power = models.IntegerField(
        verbose_name='Prioridade para exibição',
        help_text='Digite 1 para maior prioridade ou 2 para menor. Isso vai impactar a ordem de exibição na página inicial e de equipe.'
    )
    class Meta:

        verbose_name_plural = 'Posição de Membros'

    def __str__(self):
        return self.title

class Team_Member(models.Model):
    '''
    Modelo dos membros da equipe:null=True
    Nome, Url da foto, biografia, cargo, numero de projetos, horas, ano de entrada, ano de saída
    '''
    name = models.CharField(max_length=200)
    photo_url = models.ImageField(upload_to='team/', null=True, blank=True)
    biography = models.TextField(max_length=200)
    position = models.ForeignKey(Member_Position, on_delete=models.PROTECT, null=True)
    number_of_projects = models.IntegerField()
    hours = models.IntegerField()
    entry_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)
    class Meta:

        verbose_name_plural = 'Membros do Time'

    def __str__(self):
        return self.name

class Partner(models.Model):
    '''
    Modelo de Parceiros:
    Logo, Nome, Descrição, Categoria, Contato
    '''
    logo_url = models.ImageField(upload_to='partners/')
    name = models.CharField(max_length=200)
    description = models.TextField()
    projects = models.TextField(null=True)
    category = models.ForeignKey(Partner_Category, on_delete=models.PROTECT, null=True)
    contato = models.CharField(max_length=20)

    class Meta:

        verbose_name_plural = 'Parceiros'

    def __str__(self):
        return self.name

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

class Statistic(models.Model):
    '''
    Modelo para as estatísticas da página inicial:
    Valor (ex: +10, 3x, 3º) e Descrição (ex: Anos de história)
    '''
    value = models.CharField(max_length=50, verbose_name='Valor/Número')
    description = models.CharField(max_length=200, verbose_name='Descrição')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        verbose_name_plural = 'Estatísticas'
        ordering = ['order']

    def __str__(self):
        return f"{self.value} - {self.description}"

class Participant(models.Model):
    '''
    Modelo para os participantes que se inscrevem no ICC:
    Nome, Email, Curso, Semestre e Motivo
    '''
    name = models.CharField(max_length=200, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    course = models.CharField(max_length=200, verbose_name='Curso')
    semester = models.CharField(max_length=50, verbose_name='Semestre')
    reason = models.TextField(verbose_name='Por que quer entrar no ICC?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de inscrição')
    
    class Meta:
        verbose_name_plural = 'Participantes'
    
    def __str__(self):
        return self.name
    