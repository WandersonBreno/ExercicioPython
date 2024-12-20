'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
import math
area = float(input('Informe quantoas metros quadrados: '))

litros = area / 3.0
latas = math.ceil(litros / 18.0)

custo_total = latas * 80

print(f'A quantidade de latas a ser usadas é de: {latas}')
print(f'O valor à pagar é de: {custo_total:.2f}')


