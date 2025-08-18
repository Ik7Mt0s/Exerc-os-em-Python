#Escrever um programa que receba vários números inteiros no teclado.
#E no final imprimir a média dos números múltiplos de 3. Para sair digitar 0(zero).

import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    numeros = []
    divisivel_3 = []

    while True:
        try:
            entrada = input("Digite seu número ou 0 para sair\n")
            if entrada == '0':
                break
            numero = int(entrada)
            numeros.append(numero)

            if numero % 3 == 0:
                divisivel_3.append(numero)

        except ValueError:
            input("Entrada inválida. Digite um número válido\nPressione Enter para continuar...")

    if divisivel_3:
        media = sum(divisivel_3) / len(divisivel_3)
        print(f"\nNúmeros digitados..................: {numeros}")
        print(f"Números divisíveis por 3...........: {divisivel_3}")
        print(f"Média dos números divisíveis por 3.: {media:.2f}")
        saida = input('\nPressione Enter para continuar ou 0 para  ')
        if saida == '0':
            exit()
        else:
            continue
    else:
        print("\nNenhum número divisível por 3 foi digitado.")
        print(f"\nNúmeros digitados: {numeros}")
        saida = input('\nPressione Enter para continuar ou 0 para sair ')
        if saida == '0':
            exit()
        else:
            continue