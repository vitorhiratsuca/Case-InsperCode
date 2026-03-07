from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def equipe_index(request):
    return render(request, 'archive-equipe.html')

def perfil_membro(request, nome):
    return render(request, 'single-equipe.html')

def atividades(request):
    return render(request, 'atividades.html')

def parceiros_index(request):
   return render(request, 'archive-parceiro.html')

def parceiro_perfil(request, slug):
    return render(request, 'single-parceiro.html')

def participe(request):
    return render(request, 'participe.html')

def noticias(request):
    return render(request, 'archive-noticia.html')

def contato(request):
    return render(request, 'contato.html')
