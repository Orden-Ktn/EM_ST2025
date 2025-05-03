from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', views.accueil, name='accueil'),
    path('connexion/', views.login_view, name='login_view'),
    path('inscription/', views.register, name='register'), 
    path('déconnexion/', views.deconnexion, name='deconnexion'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('participant en solo/', views.liste_participant_solo, name='liste_participant_solo'),
    path('groupe participant/', views.liste_participant_groupe, name='liste_participant_groupe'),
    
    path('liste des inscriptions/', views.liste_inscriptions, name='liste_inscriptions'),
    path('inscription en solo/', views.inscription_solo, name='inscription_solo'),
    path('inscription en groupe/', views.inscription_groupe, name='inscription_groupe'),

    path('accepter inscription solo/<int:id>/', views.accepter_inscription_solo, name='accepter_inscription_solo'),
    path('accepter inscription groupe/<int:id>/', views.accepter_inscription_groupe, name='accepter_inscription_groupe'),
    path('rejeter inscription solo/<int:id>/', views.rejeter_inscription_solo, name='rejeter_inscription_solo'),
    path('rejeter inscription groupe/<int:id>/', views.rejeter_inscription_groupe, name='rejeter_inscription_groupe'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# WSGI configuration pour le projet Django hébergé sur PythonAnywhere
import os
import sys

project_home = '/home/empsbshd/EM_ST2025'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.chdir(project_home)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EM_ST2025.settings')

import django
django.setup()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()