# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condições de pagamento: à vista em dinheiro: 10% de desconto, à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.

preço = float(input('Qual o valor do produto?: '))
print('Escolha uma das formas de pagamento:')
print('[1] à vista em dinheiro com 10% de desconto')
print('[2] à vista no cartão com 5% de desconto')
print('[3] 2x no cartão sem juros')
print('[4] 3x ou mais no cartão com 20% de juros')

forma_pagamento = input('Escolha de 1 a 4 para definir a forma de pagamento: ')
print(f'Você escolheu a opção: {forma_pagamento}')

if forma_pagamento == '1':
    desconto = preço * 10 / 100
    pagamento = preço - desconto
    print(f'Você terá um desconto de: R${desconto:.2f}')
    print(f'O valor total do produto é: R${preço:.2f} e você irá pagar: R${pagamento:.2f} à vista em dinheiro.')
elif forma_pagamento == '2':
    desconto = preço * 5 / 100
    pagamento = preço - desconto
    print(f'Você terá um desconto de: R${desconto:.2f}')
    print(f'O valor total do produto é: R${preço:.2f} e você irá pagar: R${pagamento:.2f} à vista no cartão.')
elif forma_pagamento == '3':
    pagamento = preço / 2
    print(f'O valor total do produto é: R${preço:.2f} e você irá pagar em 2x de: R${pagamento:.2f} no cartão.')
elif forma_pagamento == '4':
    parcelas = int(input('Quantas parcelas deseja? (3 ou mais): '))
    if parcelas < 3:
        print("Para parcelar, é necessário escolher 3 ou mais parcelas.")
    else:
        juros = preço * 20 / 100
        pagamento = preço + juros
        parcela = pagamento / parcelas
        print(f'O valor total do produto com juros é: R${pagamento:.2f}')
        print(f'O valor de cada parcela será: R${parcela:.2f} em {parcelas}x no cartão.')
else:
    print('Opção inválida. Escolha uma opção entre 1 e 4.')