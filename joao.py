import os
from dataclasses import dataclass

@dataclass
class Familia:
    quantidade_filho : int
    salario : float
    
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_familia(dados):
    quantidade_filho = int(input("Digite a quantidade de filhos em sua família:  "))
    salario = float(input("Digite o salário de sua família: "))
    familia = Familia(quantidade_filho, salario)
    dados.append(familia)

# Salvar no arquivo.
with open("pesquisa_prefeitura.txt", "a") as f:
    f.write(f"{familia.quantidade_filho}, {familia.salario}\n")

def exibir_resultados(dados):
    if not dados:
        print("Nenhuma família foi adicionada.")
        return
    total_familias = len(dados)
    salarios = [familia.salario for familia in dados]
    filhos = [familia.quantidade_filhos for familia in dados]
    media_salario = sum(salarios) / total_familias
    media_filhos = sum(filhos) / total_familias
    maior_salario = max(salarios)
    menor_salario = min(salarios)

print(f"Total de famílias: {total_familias}")
print(f"Média do salário da população: {media_salario:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Maior salário: {maior_salario:.2f}")
print(f"Menor salário: {menor_salario:.2f}")

def carregar_dados():
    dados = []

# Tentar abrir o arquivo e carregar os dados.
arquivo = open("pesquisa_prefeitura.txt", "r")
for linha in arquivo:
    quantidade_filho, salario = linha.strip().split(",")
    dados.append(Familia(int(quantidade_filho), float(salario)))
    arquivo.close()
    return dados

def main():
    if not os.path.isfile("pesquisa_prefeitura.txt"):
        open("pesquisa_prefeitura.txt", "w").close()
        dados = carregar_dados()

while True:
    clear_terminal()
    print("Menu.")
    print("1 - Adicionar família")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
    escolha = input("Escolha uma opção: ")
    if escolha == 1:
        adicionar_familia(dados)
    elif escolha == 2:
        exibir_resultados(dados)
    elif escolha == 3:
        break
    else:
        print("Opção inválida, tente novamente.")
        main()