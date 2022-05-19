numero = int(input('Digite um número para saber se é par ou impar: '))
verificacao = numero % 2

if verificacao == 0:
    print(f'O número {numero} é um Número par')
else:
    print(f'O número {numero} é um Número impar')