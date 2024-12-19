# Crie um programa que faça o computador jogar Pedra, Papel, Tesoura com você.

from random import randint
from time import sleep

num = randint(0, 2)

print('Suas opções são:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
escolha = int(input('Qual é a sua jogada? '))
print('Pedra...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!!!')

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

if escolha < 0 or escolha > 2:
    print("Jogada inválida! Tente novamente.")
else:
    opcao_usuario = opcoes[escolha]
    opcao_comp = opcoes[num]

    print('-=' * 13)
    print(f'O computador jogou {opcao_comp}')
    print(f'Você jogou {opcao_usuario}')
    print('-=' * 13)

    if escolha == num:
        print('Empate!')
    elif (escolha == 0 and num == 2) or (escolha == 1 and num == 0) or (escolha == 2 and num == 1):
        print('Você venceu!')
    else:
        print('O computador venceu!')