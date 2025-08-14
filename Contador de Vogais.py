import os, unicodedata

while True:        
    os.system('cls' if os.name == 'nt' else 'clear')

    palavra = input('Digite a palavra que será contada as vogais\n')

    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    
    for letras in palavra:
        # Normaliza a letra para forma NFD (decompondo acentos)
        letra_normalizada = unicodedata.normalize('NFD', letras.lower())
        # Pega apenas a primeira parte (vogal base, ignorando o acento)
        vogal_base = letra_normalizada[0] if len(letra_normalizada) > 0 else ''

        if vogal_base == 'a':
            contador_a += 1
            
        elif vogal_base == 'e':
            contador_e += 1
        
        elif vogal_base == 'i':
            contador_i += 1
            
        elif vogal_base == 'o':
            contador_o += 1
            
        elif vogal_base == 'u':
            contador_u += 1 
            
    print(f'Mensagem: {palavra}')
    print(f'A: {contador_a}')
    print(f'E: {contador_e}')
    print(f'I: {contador_i}')
    print(f'O: {contador_o}')
    print(f'U: {contador_u}')

    saida = input('\nPressione Enter para continuar ou S para sair\n')
    if saida.lower() == 's':
        exit()
    else:
        continue