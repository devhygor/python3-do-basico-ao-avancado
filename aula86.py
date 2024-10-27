"""
Exercício
Exiba os indices da lista
Maria
Helena
Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

# for indice in indices:
#     print(f'{indice} - {lista[indice]}')

# for indice, nome in zip(indices, lista):
#     print(f'{indice} - {nome}')

# for nome in lista:
#     print(f'{lista.index(nome)} - {nome}')

for indice, nome in enumerate(lista):
    print(f'{indice} - {nome}')