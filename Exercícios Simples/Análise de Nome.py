# Escrever um programa que receba um nome.
# a) Que conte o número de vogais existentes nele.
# b) O programa deverá imprimir o número total de caracteres do nome.
# c) Quantas vogais e a respectiva porcentagem das vogais em relação ao total de caracteres.
import os, unicodedata

while True:
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            nome = input('Digite um nome:\n').strip() #.strip() é usado para remover espaços em branco (ou outros caracteres especificados) do início e do final de uma string.
            if not nome:
                input('Por favor digite um nome. Pressione Enter para continuar...')
                continue
            elif not any(c.isalpha() for c in nome):
                input('\nEntrada inválida: Digite um nome com letras. Pressione Enter para continuar...')
                continue
            elif any(c.isdigit() for c in nome):
                input("Números não são permitidos no nome. Pressione Enter para continuar...")
            else:
                break
        except Exception as e:
            input('\nErro inesperado. Pressione Enter para tentar novamente...')
            
    vogais = 0
    total_de_letras = 0

    for letras in nome:
        if letras == ' ': #Ignora o espaço na contagem 'for'
            continue

        total_de_letras += 1

        letra_normalizada = unicodedata.normalize('NFD', letras.lower())
        vogal_base = letra_normalizada[0] if len(letra_normalizada) > 0 else ''

        if vogal_base in {'a', 'e', 'i', 'o', 'u'}:
            vogais += 1

        porcentagem = (vogais/total_de_letras) * 100

    print(f'Nome.....................: {nome}')
    print(f'Número de vogais.........: {vogais}')
    print(f'Número de caracteres.....: {total_de_letras}')
    print(f'Porcentagem vogais/total.: {porcentagem:.2f}%')

    saida = input('\nPressione Enter para continuar ou S para sair\n')
    if saida.lower() == 's':
        exit()
    else:
        continue