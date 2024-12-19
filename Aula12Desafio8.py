# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso Ideal
# 25 a 30: Sobrepeso
# 30 a 40: Obesidade
# Acima de 40: Obesidade Mórbida
# IMC = peso / (altura x altura)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    status = 'Abaixo do Peso'
elif 18.5 <= imc < 25:
    status = 'Peso Ideal'
elif 25 <= imc < 30:
    status = 'Sobrepeso'
elif 30 <= imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'

print(f'Seu peso é {peso:.2f}kg, seu IMC é {imc:.1f} e seu status é: {status}!')