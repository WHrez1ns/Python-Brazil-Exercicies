# Faça um Programa que peça dois números e imprima o maior deles:

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
if (num1 > num2):
    print('O número', num1, 'é maior que o número', num2)
elif (num1 < num2):
    print('O número', num2, 'é maior que o número', num1)
else:
    print('Os números são iguais!')