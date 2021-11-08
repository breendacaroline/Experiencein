from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id ==1:
        perfil = Perfil('Brenda Caroline', 'brendacaroline@gmail.com', '535698', 'IFB')

    if perfil_id == 2:
        perfil = Perfil('Sabrina', 'sabrinasousa@gmail.com', '587946', 'Amazon')

    return render(request, 'perfil.html', {'perfil' : perfil})