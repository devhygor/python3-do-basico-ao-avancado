"""
Faça um programa que peça ao usuario para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

def par_ou_impar():
    num = int(input("Digite um número inteiro: "))
    if not num:
        print("Não é um número inteiro.")
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é impar.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

def hora():
    hora = int(input("Digite a hora: "))
    if 0 <= hora <= 11:
        print("Bom dia!")
    elif 12 <= hora <= 17:
        print("Boa tarde!")
    elif 18 <= hora <= 23:
        print("Boa noite!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
def tamanho_nome():
    nome = input("Digite seu nome: ")
    if len(nome) <= 4:
        print("Seu nome é curto.")
    elif 5 <= len(nome) <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")

if __name__ == "__main__":
    opcao_selecionada = input('1 => par ou impar\n'
                              '2 => hora\n'
                              '3 => tamanho do nome\n'
                              'Digite uma das opções para executar o codigo: '
                            )
    if  opcao_selecionada == '1':
        par_ou_impar()
    elif opcao_selecionada == '2':
        hora()
    elif opcao_selecionada == '3':
        tamanho_nome()
    else:
        print('Opção inválida')