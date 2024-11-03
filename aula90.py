"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Nçao permita que o programa quebre com
erros de indices inexistentes na lista.
"""
import os

lista_compras = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        item_input = input('Acrescente um item na sua lista: ')
        lista_compras.append(item_input)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except:
            print('Não foi possivel apagar este índice')

    elif opcao == 'l':
        os.system('clear')
        if len(lista_compras) == 0:
            print('Nada para listar')
            
        for index, item_lista_compras in enumerate(lista_compras):
            print(f'{index} - {item_lista_compras}')

    else:
        print('Por favor, escolha i, a ou l.')

