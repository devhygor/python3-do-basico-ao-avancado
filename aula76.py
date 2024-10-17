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
Faça a contagem de tentativas do seu 
usuário.
"""

palavra_secreta = input('QUAL SERA A PALAVRA SECRETA? ').upper()
palavra_corrigida = ''

tentativas = 0

# while len(palavra_corrigida) != len(palavra_secreta):
while True:
    tentativas += 1
    print(f'Tentativa n° {tentativas}')
    letra = input('DIGITE UMA LETRA: ').upper()
    
    if len(letra) != 1:
        print('DIGITE APENAS UMA LETRA!')
        continue

    if letra in palavra_secreta:
        palavra_corrigida += letra
        if len(palavra_corrigida) == 1:
            print(f'Letra correta: "{letra}"\n')
        else:
            print(f'Letras corretas: "{palavra_corrigida}"\n')
        
        for letra_secreta in palavra_secreta:
            if letra_secreta in palavra_secreta:
                print(letra_secreta)
    else:
        print(f'A Letra "{letra}", nao existe na palavra secreta!\n')
else:
    print(f'Todas as letras da palavra secreta foram digitadas! {palavra_corrigida}')
    print(f'A Palavra secreta era {palavra_secreta}')

