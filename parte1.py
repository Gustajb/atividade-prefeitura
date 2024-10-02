import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Familia:
    quantidade_filhos: int
    salario: float


# Lista de de alunos.
lista_de_familias = []
total_familias = 0
soma_salario = 0
contador_familias = 0
contador_filhos = 0
contador_filhos2 = 0

print("""
      Código | Descrição
      1      | Adicionar família
      2      | Exibir resultados
      3      | Sair
      """)

def menu():
    print("=== EXIBINDO MENU ===")
    print("""
        Código | Descrição
        1      | Adicionar Família
        2      | Exibir resultados 
        3      | Sair
        """)

       

while True:
    opcao = int(input("Digite o código para escolher uma opção: "))
    break

def limpar_terminal():
    os.system("cls || clear")

def solicitando_dados():
    print("\n=== Solicitando dados da família ===")

while True:
        familia = Familia(
            quantidade_filhos = int(input("Digite sua quantidade de filhos: ")),
            salario = float(input("Digite seu salário: ")))
        break

soma_salario += familia.salario
lista_de_familias.append(familia)

def exibindo_resultados():
    print("\n=== Exibindo dados dos alunos ===")
    for familia in lista_de_familias:
        print(f"Quantidade de filhos: {familia.quantidade_filhos}")
        print(f"Salário: {familia.salario}")

match(opcao):
    case 1:
        limpar_terminal()
        resultado = solicitando_dados()
        print(f"{resultado}")
    case 2:
        limpar_terminal
        resultado = exibindo_resultados()
        print(f"{resultado}")
    case 3:
        print("=== FIM ===")

# Definindo arquivo para salvar os dados.
nome_do_arquivo = "pesquisa.prefeitura.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "a") as arquivo_familias:
    # Percorrendo vetor/lista.
    for familia in lista_de_familias:
        # Escrevendo no arquivo uma linha de cada vez.
        arquivo_familias.write(f"{familia.quantidade_filhos}, {familia.salario}\n")

# Fechar conexão com o arquivo.
arquivo_familias.close()
print("\n=== Dados dos alunos salvo com sucesso! ===")


# Lendo dados de um arquivo.
# Limpando a lista de alunos.
lista_de_familias = []

print("\n=== Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        quantidade_filhos, salario = linha.strip().split(",")
        lista_de_familias.append(Familia(quantidade_filhos= int(quantidade_filhos), salario= float(salario)))

# Fechar conexão com o arquivo.
arquivo_familias.close()

for familia in lista_de_familias:
    contador_filhos2 += contador_filhos
    media = contador_filhos2/contador_filhos

print("\n\n=== Exibindo dados das famílias do arquivo ===")
for familia in lista_de_familias:
    print(f"Quantidade de filhos: {familia.quantidade_filhos}")
    print(f"Salário: {familia.salario}")
    print(f"Número de famílias: {lista_de_familias}")
    print(f"Média do número de filhos: {media}")
    print(f"Média dos salários: {familia.salario}")



