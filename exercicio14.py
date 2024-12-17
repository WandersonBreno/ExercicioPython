'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido
pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 
por quilo excedente. João precisa que você faça um programa que leia a variável peso 
(peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do 
programa com as mensagens adequadas.'''

print("Bem vindo João")

peso_peixe = float(input("Informe quantos quilos de peixe foi pego: "))
excesso = 0
multa = 0 

if peso_peixe > 50:
   excesso = peso_peixe - 50
   multa = excesso * 4
   print(f'O peso em kg de excesso dos peixes é de: {excesso} kg será pago uma multa de: R$ {multa}')
else:
   print("Não é necessário pagar multa. ")