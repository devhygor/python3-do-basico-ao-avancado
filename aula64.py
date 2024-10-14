"""
Iterando strings com while
"""
nome = 'Hygor Melo Rocha'
tamanho_nome = len(nome)
indice = 0
nova_string = ''

while indice < tamanho_nome:
    letra_posicao = nome[indice]
    nova_string += f'*{letra_posicao}'
    indice += 1

print(nova_string)