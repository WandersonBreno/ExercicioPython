#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Cálculo de ganho mensal.")

ganho_por_hora = float(input("Digite o seu ganho por hora trabalhada: "))
horas_trabalhadas = float(input("Digite quantas horas trabalhou no mês: "))
ganho_total = ganho_por_hora * horas_trabalhadas

print(f'Seu salário de acordo com os dados informados é: {ganho_total}')