#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

area = float(input("Infomr a base ou altura da área m²: "))

calculo_area = area * area
dobro_area = calculo_area * 2

print(f'A área do quadrado é: {calculo_area} m²')
print(f'O dobro da área do quadrado é: {dobro_area} m²')