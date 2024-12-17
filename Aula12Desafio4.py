# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano_nasc = int(input('Digite o ano de seu nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nasc

if idade == 18:
    print('Você tem 18 anos e já pode realizar seu alistamento militar.')
elif idade < 18:
    falta = 18 - idade
    print(f'Você tem {idade} anos e ainda não atingiu a idade certa para o alistamento militar.')
    print(f'Resta{"m" if falta > 1 else ""} {falta} ano{"s" if falta > 1 else ""} para você atingir a idade de alistamento.')
else:
    passou = idade - 18
    print(f'Você tem {idade} anos e já pass{"aram" if passou > 1 else "ou"} {passou} ano{"s" if passou > 1 else ""} do prazo de alistamento.')