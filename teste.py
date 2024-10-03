import os

def limpar_terminal():
    os.system("cls || clear")

def salvar_dados(dados):
    with open("pesquisa_prefeitura.txt," "w") as arquivo:
        for familia in dados:
            arquivo.write(f"{familia['salario']},{familia['filhos']}")

def ler_dados():
    dados = []
    if os.path.exists("pesquisa_prefeitura.txt"):
        with open("pesquisa_prefeitura.txt", "r") as arquivo:
            for linha in arquivo:
                salario, filhos = linha.strip().split(',')
                dados.append({'salario': float(salario), 'filhos': int(filhos)})
    return dados

def adicionar_familia(dados):
    salario = float(input("Digite o salário da família: "))
    filhos = int(input("Digite o número de filhos da família: ")) 
    dados.append({'salario': salario, 'filhos': filhos})
    salvar_dados(dados)

def exibir_resultados(dados):
    if not dados:
        print("Nenhuma família cadastrada.")
        return
    
    total_familias = len(dados)
    media_salario = sum(f['salario'] for f in dados) / total_familias
    media_filhos = sum(f['filhos'] for f in dados) / total_familias
    maior_salario = max(f['salario'] for f in dados) 
    menor_salario = min(f['salario'] for f in dados) 

    print(f"Total de famílias: {total_familias}")
    print(f"Média do salário da população: R$ {media_salario}")
    print(f"Média de filhos: {media_filhos}")
    print(f"Maior salário: R$ {maior_salario}")
    print(f"Menor salário: R$ {menor_salario}")
    
def main():
    dados = ler_dados()

    while True:
        limpar_terminal()
        print("=== Menu ===")
        print("""
        Código | Descrição
        1      | Adicionar Família
        2      | Exibir resultados 
        3      | Sair
        """)


opcao = int(input("Digite o código para escolher uma opção: "))

if opcao == "1":
            adicionar_familia(dados)
elif opcao == "2":
            exibir_resultados(dados)
            input("Pressione Enter para continuar.")
elif opcao == "3":
            break
else: 
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()