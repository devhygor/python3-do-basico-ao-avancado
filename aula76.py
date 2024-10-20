"""
Faça um jogo para o usuário adivinhar qual 
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade 
para o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, voce
vai conferir se a letra digitada está 
na palavra secreta.
    - Se a letra estiver na 
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de numero_tentativas do seu 
usuário.
"""
import os


palavra_secreta = input('QUAL SERA A PALAVRA SECRETA? ').upper()
os.system('clear')
letras_acertadas = ''
numero_tentativas = 0

while True:
    palavra_corrigida = ''
    numero_tentativas += 1
    print(f'Tentativa n° {numero_tentativas}')
    letra_digitada = input('DIGITE UMA LETRA: ').upper()
    
    if len(letra_digitada) != 1:
        print('DIGITE APENAS UMA LETRA!')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_corrigida += letra_secreta
        else:
            palavra_corrigida += '*'

    print(f'Palavra formada: {palavra_corrigida}\n')
    
    if palavra_corrigida == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A palavra era "{palavra_secreta}"')
        print(f'Total de tentativas: {numero_tentativas}\n')

        palavra_secreta = input('QUAL SERA A PALAVRA SECRETA? ').upper()
        letras_acertadas = ''
        numero_tentativas = 0