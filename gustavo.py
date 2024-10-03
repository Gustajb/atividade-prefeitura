import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pesquisa:
    nome: str
    numero_de_filhos: int
    salario: float

def media(a,b):
    mediafim = a/b
    return mediafim
def maior_menor(a):
    menor = min(lista_de_salarios)
    maior = max(lista_de_salarios)
    return maior, menor

lista_de_familias = []
lista_de_salarios = []

numero_familias = 0
contador_salario = 0
contador_filhos = 0

while True:
    print("""
            === Menu ===
    |Código |   Descrição       |
    |   1   | Adicionar família |
    |   2   | Exibir resultados |
    |   3   | Sair              |
          """)
    menu = int(input("Digite uma opção: "))
    os.system("cls || clear")