from django.contrib import admin
from django.urls import path
from customers import views

app_name = 'customers'

urlpatterns = [
    path('voitures/', views.ajouter, name='voitures'),
    path('voitures/supprimer/<int:voiture_id>', views.supprimer_voiture, name = 'supprimer',),
    path('voitures/modifier/<int:voiture_id>', views.modifier_voiture, name='modifier', ),

    path('locations/', views.location, name='locations'),
    path('locations/supprimer/<int:client_id>', views.supprimer_client, name='supprimer_client', ),
    path('locations/modifier/<int:client_id>', views.modifier_client, name='modifier_client', ),
    path('locations/details/<int:client_id>', views.details, name='details_client', ),

    path('historique/', views.historique, name='historique'),

    path('', views.Accueil, name='accueil'),


]