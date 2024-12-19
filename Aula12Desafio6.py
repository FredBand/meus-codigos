# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a sua idade.
# Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JUNIOR, Até 25 anos: SÊNIOR, Acima: MASTER.

from datetime import datetime

ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = datetime.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'O atleta tem {idade} anos de idade. Sua categoria é: {categoria}!')