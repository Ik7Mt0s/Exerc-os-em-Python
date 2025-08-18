import os
while True:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mensagem = input('Digite uma mensagem de até 40 caracteres:\n')
        # Conta apenas caracteres alfabéticos
        qtd_letras = sum(c.isalpha() for c in mensagem)
        if qtd_letras <= 40:
            break
        else:
            input('\nMensagem ultrapassou o limite de caracteres\nPressione Enter e digite novamente ')
    
    for c in mensagem:
        if c.isalpha():  # Mostra só se for letra
            print(c)

    continuaçao = input('\nPressione Enter para continuar ou S para sair')
    if continuaçao.lower() == 's':
        exit()
    else:
        continue