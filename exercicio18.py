'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download 
do arquivo usando este link (em minutos).'''

tamanho_mbp = float(input("Informe o tamanho do download em mbp: "))
velocidade_link = float(input("Informe a velocidade do link em Mpbs: "))

tempo = tamanho_mbp / velocidade_link
min = tempo / 60
print("O tempo aproximado de download do arquivo será de: %.2f minutos" %min)