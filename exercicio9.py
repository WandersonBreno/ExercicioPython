#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a 
#temperatura em graus Celsius.C = 5 * ((F-32) / 9).

Temp_F = int(input("Digite quantos graus em Fahrenheit: "))

print ('Temperatura em Celsius: %.2f' %(5 * (Temp_F-32) / 9))