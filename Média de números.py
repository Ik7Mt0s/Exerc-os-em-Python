#Fazer um programa que realize a média aritimética e a média ponderada que quantos números o usuário quiser
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Para obter a média de números digite 1 ")
    print("Para sair do programa digite 2 ")
    
    num = input("Digite sua escolha: ")

    if num == '1':
        numero = []
        pesos = []

        print("           Digite o tipo de média           ")
        print("1-Média Aritmética   ||   2-Média Ponderada")
        tipo_media = input()

        if tipo_media == '1':
            while True:
                entrada = input("Digite seu número ou F para finalizar: ")
                if entrada.lower() == 'f':
                    break
                try:
                    numero.append(float(entrada))
                except ValueError:
                    print("Entrada inválida. Digite um número válido.")

            if len(numero) == 0:
                print("Nenhum número foi inserido.")
            else:
                media_aritmetica = sum(numero) / len(numero)
                print(f'\nNúmeros: {numero}')
                print(f'Quantidade: {len(numero)}')
                print(f"Média aritmética: {media_aritmetica}")
            input('\nPressione Enter para voltar ao menu principal...')

        elif tipo_media == '2':
            while True:
                entrada = input("Digite seu número ou F para finalizar: ")
                if entrada.lower() == 'f':
                    break
                try:
                    numero.append(float(entrada))
                except ValueError:
                    print("Número inválido.")
                    continue

                peso = input("Digite o peso correspondente a esse número: ")
                try:
                    pesos.append(float(peso))
                except ValueError:
                    print("Peso inválido.")
                    numero.pop()
                    continue

            if len(numero) == 0 or sum(pesos) == 0:
                print("Não é possível calcular média.")
            else:
                media_ponderada = sum([numero[i] * pesos[i] for i in range(len(numero))]) / sum(pesos)
                print(f'\nNúmeros: {numero}')
                print(f'Pesos: {pesos}')
                print(f'Soma dos pesos: {sum(pesos)}')
                print(f"Média ponderada: {media_ponderada}")
            input('\nPressione Enter para voltar ao menu principal...')

        else:
            print("Digite um valor válido (1 ou 2).")
            input("\nPressione Enter para retornar.")

    elif num == '2':
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
        input("\nPressione Enter para retornar.")
