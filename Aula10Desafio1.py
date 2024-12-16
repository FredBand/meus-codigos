# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça ao usuário para
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint # Gera um número aleatório inteiro.
from time import sleep # O código aguarda determinado tempo.

num = randint(0, 5)

num1 = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(2)
if num1 == num:
    print('Você acertou!')
    print(f'Eu pensei no número: {num}')
else:
    print(f'Ganhei! Eu pensei no número: {num} e não em: {num1}!')
    print('Tente novamente!')