from django.urls import path

from . import views

urlpatterns = [
    # Landing page
    path('', views.index, name='index'),

    # Equipe
    path('equipe/', views.equipe_index, name='equipe'),

    # Equipe Single
    path('equipe/<slug:nome>/', views.perfil_membro, name='perfil_membro'),

    # Atividades 
    path('atividades/', views.atividades, name='atividades'),

    # Parceiros
    path('parceiros/', views.parceiros_index, name='parceiros'),

    # Parceiro Single
    path('parceiros/<slug:slug>/', views.parceiro_perfil, name='perfil_parceiro'),

    # Processo seletivo 
    path('participe/', views.participe, name='participe'),

    # Noticias 
    path('noticias/', views.noticias, name='noticias'),

    # Contato
    path('contato/', views.contato, name='contato'),
]