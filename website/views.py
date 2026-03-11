from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .models import Partner, Partner_Category, Team_Member, Member_Position, Statistic, Activity, Participant

@require_http_methods(["GET"])
def index(request):
    members = Team_Member.objects.filter(exit_date__isnull=True).order_by('position__power', 'name')[:6]
    statistics = Statistic.objects.all().order_by('order')
    return render(request, 'index.html', {'members': members, 'statistics': statistics, 'partners': Partner.objects.all()})

@require_http_methods(["GET"])
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

@require_http_methods(["GET"])
def perfil_membro(request, nome):
    member = get_object_or_404(Team_Member, name=nome)
    return render(request, 'single-equipe.html', {'member': member})

def atividades(request):
    activities = Activity.objects.all()
    return render(request, 'atividades.html', {'activities': activities})

@require_http_methods(["GET"])
def parceiros_index(request):
    partners = Partner.objects.all()
    categories = Partner_Category.objects.all()
    return render(request, 'archive-parceiro.html', {
        'partners': partners,
        'categories': categories
    })

def parceiro_perfil(request, id):
    partner = get_object_or_404(Partner, id=id)
    activities = Activity.objects.filter(responsible_partner=partner)
    return render(request, 'single-parceiro.html', {'partner': partner, 'activities': activities})  

def participe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        semester = request.POST.get('semester')
        reason = request.POST.get('reason')
        
        if all([name, email, course, semester, reason]):
            Participant.objects.create(
                name=name,
                email=email,
                course=course,
                semester=semester,
                reason=reason
            )
            return render(request, 'participe.html', {'submission_success': True})
    
    return render(request, 'participe.html')

def noticias(request):
    return render(request, 'archive-noticia.html')

def contato(request):
    return render(request, 'contato.html')

