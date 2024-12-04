'''Faça um Programa que peça a temperatura em graus Celsius,
  transforme e mostre em graus Fahrenheit.'''

Celsius = float(input("Digite quantos graus Celsius: "))

Fahrneheit = (Celsius * 1.8) + 32

print(f'A conversão de Celsius para Fahrneheit é: {Fahrneheit:.2f}')