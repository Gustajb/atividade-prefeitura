import os
from dataclasses import dataclass

match menu:
        case 1:
            familia = Pesquisa(
                nome = input("Digite o seu nome: "),
                numero_de_filhos = int(input("Digite o número de filhos na família: ")),
                salario = float(input("Digite o salário da família: R$ "))
            )
            lista_de_familias.append(familia)
            lista_de_salarios.append(familia.salario)
            contador_salario += 1
            numero_familias += 1

            os.system("cls || clear")

        case 2:
            print("\n=== Exibindo resultados ===")
            for familia in lista_de_familias:
                print(f"Nome: {familia.nome}")
                print(f"Número de filhos: {familia.numero_de_filhos}")
                print(f"Salário: R$ {familia.salario}")

            if contador_salario > 1:

                maior_salario, menor_salario = maior_menor(lista_de_salarios)
                media_salario = media(sum(lista_de_salarios),(len(lista_de_salarios)))
                print(f"\nMaior salário: R$ {maior_salario:.2f}")
                print(f"\nMenor salário: R$ {menor_salario:.2f}")
                print(f"\nA média dos salários foram: {media_salario}")
            if numero_familias > 1:
                
                quantidade_familias = len(lista_de_familias)
                contador_filhos = 0
                for familia in lista_de_familias:
                    contador_filhos += familia.numero_de_filhos

                media_filhos = media(contador_filhos, quantidade_familias)
                print(f"\nMédia de filhos por família: {media_filhos:.2f}")

        case 3:
            nome_do_arquivo = "pesquisa_prefeitura.txt"
            with open(nome_do_arquivo, "a") as pesquisadts:
                for familia in lista_de_familias:
                    pesquisadts.write(f"{familia.nome}, {familia.salario}, {familia.numero_de_filhos}\n")
            break

with open (nome_do_arquivo, "r") as todos_alunos:
    for linha in lista_de_familias:
        nome, salario, numero_de_filhos = linha.strip().split(",")
        lista_de_familias.append(pesquisadts(nome=nome, salario=float(salario, numero_familias=int(numero_de_filhos))))

print("\n=== Exibindo dados das famílias ===")
for familia in lista_de_familias:
    print(f"Nome: {familia.nome}")
    print(f"Número de filhos: {familia.numero_de_filhos}")
    print(f"Salário: {familia.salario}")

pesquisadts.close()