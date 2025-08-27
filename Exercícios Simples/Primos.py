#Criar um programa que receba um número e
#a)Verfica se ele é primo
#b)Mostra todos os números primos entre 2 e o número recebido
import os
#Função para verificar se o número é primo
def verificar_primos(n):
    divisoes = 0
    if n > 1:
        for i in range(1, n):
            if n % i == 0:
                divisoes += 1
    if divisoes == 1:
        print(f"O número {n} é primo")
    else:
        print(f"O número {n} não é primo")

#Função para selecionar números primos
def todos_os_primos(n):
    primos = [True] * (n+1)
    primos[0], primos[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primos[i]:
            for j in range(i*i , n+1, i):
                primos[j] = False
    for i in range(n+1):
        if primos[i]:
            print(i)

while True:
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            numero = int(input("Digite o número a ser verificado se é primo:\n"))
            break
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
            input('\nPressione Enter para selcionar uma opção novamente ')
            continue
   
    verificar_primos(numero)

    ver_primos_anteriores = input(f"\nDeseja ver todos os números primos entre 2 e {numero}?\n\nPressione C para continuar ou S para sair: ")
    if ver_primos_anteriores.lower() == 'c':
        if numero >= 2:
            todos_os_primos(numero)
        else:
            print(f"\nNão existe primos entre 2 e {numero}")
            
    saida = input('\nPressione Enter para continuar ou S para sair ')
    if saida.lower() == 's':
        break
    else:
        continue