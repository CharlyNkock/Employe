from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_employe, name="liste_employes"),
    path("ajouter/", views.ajouter_employe, name="ajouter_employes"),
    path("modifier/<int:id>/", views.modifier_employe, name="modifier_employes"),
    path("supprimer/<int:id>/", views.supprimer_employe, name="supprimer_employes"),
]
