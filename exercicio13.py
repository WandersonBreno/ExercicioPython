'''Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a)Para homens: (72.7*h) - 58
b)Para mulheres: (62.1*h) - 44.7'''

print("Bem-vindo ao programa de cálculo de peso ideal")

altura= float(input("Informe a sua altura: "))
sexo = input("Informe o seu sexo, (M) para masculino (F) para feminino: ")

if sexo == 'M':
    print(f'Seu peso ideal é: {(72.7 * altura) - 58}')

elif sexo == 'F':
    print(f'Seu peso ideal é: {(62.1 * altura) - 44.7}')

else:
    print("Dados incorretos, tente novamente.")