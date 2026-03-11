from django.shortcuts import render, get_object_or_404
from .models import Partner, Partner_Category, Team_Member, Member_Position, Statistic

# Create your views here.
def index(request):
    members = Team_Member.objects.filter(exit_date__isnull=True).order_by('position__power', 'name')[:6]
    statistics = Statistic.objects.all().order_by('order')
    return render(request, 'index.html', {'members': members, 'statistics': statistics})

def equipe_index(request):
    members = Team_Member.objects.all().order_by('position__power', 'name')
    positions = Member_Position.objects.all().order_by('power')
    entry_years = (
        Team_Member.objects
        .dates('entry_date', 'year')
        .values_list('entry_date__year', flat=True)
        .distinct()
        .order_by('entry_date__year')
    )
    return render(request, 'archive-equipe.html', {
        'members': members,
        'positions': positions,
        'entry_years': entry_years,
    })

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

