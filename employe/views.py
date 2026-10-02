from django.shortcuts import get_object_or_404, render, redirect
from .models import Employe
from .forms import EmployeForm


def list_employe(request):
    employes = Employe.objects.all()
    return render(request, 'employes/list.html', {'employes' : employes})


def ajouter_employe(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    return render(request, 'employes/formulaire.html', {'form' : form})

def modifier_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    form  = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    return render(request, 'employes/formulaire.html', {'form' : form})

def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    if request.method == "POST":
        employe.delete()
        return redirect('liste_employes')
    return render(request, 'employes/confirm.html', {'employe' : employe})