from django.shortcuts import render, get_object_or_404
from .models import Partner, Partner_Category, Team_Member

# Create your views here.
def index(request):
    return render(request, 'index.html')

def equipe_index(request):
    members = Team_Member.objects.all()
    return render(request, 'archive-equipe.html', {'members': members})

def perfil_membro(request, nome):
    member = get_object_or_404(Team_Member, name=nome)
    return render(request, 'single-equipe.html', {'member': member})

def atividades(request):
    return render(request, 'atividades.html')

def parceiros_index(request):
    partners = Partner.objects.all()
    categories = Partner_Category.objects.all()
    return render(request, 'archive-parceiro.html', {
        'partners': partners,
        'categories': categories
    })

def parceiro_perfil(request, id):
    partner = get_object_or_404(Partner, id=id)
    return render(request, 'single-parceiro.html', {'partner': partner})

def participe(request):
    return render(request, 'participe.html')

def noticias(request):
    return render(request, 'archive-noticia.html')

def contato(request):
    return render(request, 'contato.html')

