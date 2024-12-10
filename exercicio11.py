'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
   1° o produto do dobro do primeiro com metade do segundo .
   2° a soma do triplo do primeiro com o terceiro.
   3º o terceiro elevado ao cubo.
'''
numero1 = int(input("Digite o 1º número inteiro: "))
numero2 = int(input("Digite o 2° número inteiro: "))
numero3 = float(input("Digite um número real: "))

questao1 = (numero1 *2) + (numero2 / 2)
questao2 = (numero1 *3) + numero3
questao3 = numero3 **3

print(f'O dobro do primeiro número mais a metade do segundo número é: {questao1}')
print(f'A soma do triplo do primeiro número mais o terceiro número é: {questao2}')
print(f'O terceiro número elevado ao cubo é: {questao3}')