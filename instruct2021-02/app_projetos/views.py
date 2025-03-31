from django.shortcuts import render, redirect
from django.http import HttpResponse
from logging import exception
import requests
from importlib.metadata import version

from django.shortcuts import render, redirect
from .models import Colecao


def criar_projeto(request):
    if request.method == 'POST':
        # Pegando os dados do formulário HTML
        nome = request.POST.get('nome')
        pacotes = request.POST.get('pacotes')
        versao = request.POST.get('versao')

        novo_projeto = Colecao.objects.create(
            nome = nome,
            pacotes = pacotes,
            versao = versao
        )

        # Redireciona para uma página de sucesso
        return redirect('detalhes_projeto', pk=novo_projeto.pk)

    # Se for GET, mostra o formulário vazio
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def versao_pacote(pac):
    try:
        return version(pac)
    except Exception as e:
        return e

def checar_versao(package_name, target_version):
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        data = response.json()
        available_versions = list(data["releases"].keys())
        if target_version in available_versions:
            return True
        else:
            print("error: One or more packages doesn't exist")
            exit(1)
    except Exception:
        print("error: One or more packages doesn't exist")
        exit(1)
