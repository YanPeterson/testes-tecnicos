import os
from logging import exception
import requests

from importlib.metadata import version

class Colecao():

    def __init__(self, nome, pacotes):
        self.nome = nome
        self.pacotes = pacotes

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
def criar_projeto():
    nome = input('Digite o nome do projeto: ')
    pacotes_lista = []
    projeto1 = None
    x = 1
    while x == 1:
        pac = input('Digite o nome do seu pacote: ')
        versao = input('Caso saiba a versão do pacote digite, se não digite 0: ')
        if versao == '0':
            versao = versao_pacote(pac)
        checar_versao(pac, versao)
        x = int(input('Caso tenha mais algum pacote digite 1, se não digite qualquer tecla: '))
        pacotes_lista.append({pac : versao})
        projeto1 = Colecao(nome, pacotes_lista)
    else:
        print('Projeto adicionado com sucesso!')

#print(f'name: {projeto1.nome}\npackages: {projeto1.pacotes}')
