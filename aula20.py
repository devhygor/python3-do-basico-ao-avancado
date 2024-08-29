# Exercicio de programação com if e comparação

# Exiba primeiro o valor que for maior

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O valor {primeiro_valor=} é maior que {segundo_valor=}.')
elif primeiro_valor < segundo_valor:
    print(f'O valor {segundo_valor=} é maior que {primeiro_valor=}.')
elif primeiro_valor == segundo_valor:
    print(f'Os valores sao iguais')