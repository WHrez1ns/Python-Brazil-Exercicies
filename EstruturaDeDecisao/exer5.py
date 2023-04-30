# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#	- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#	- A mensagem "Reprovado", se a média for menor do que sete;
#	- A mensagem "Aprovado com Distinção", se a média for igual a dez.

try:
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
except ValueError:
    print("Por favor, insira um valor numérico válido para as notas!")
else:
    media = (nota1 + nota2) / 2
    if media >= 7:
        if media == 10:
            print("Aluno APROVADO COM DISTINÇÃO!")
        else:
            print("Aluno APROVADO!")
    else:
        print("Aluno REPROVADO!")
    print("Média: {:.1f}".format(media))