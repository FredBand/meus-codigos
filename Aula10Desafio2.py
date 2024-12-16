# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

vel = float(input('Qual a velocidade atual do carro?: '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Parabéns, você está respeitando o limite de velocidade!')
else:
    print('Você excedeu o limite de velocidade e foi MULTADO!')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')