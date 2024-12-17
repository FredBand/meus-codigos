# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.

casa = float(input('Informe o valor da casa:R$'))
salario = float(input('Qual o valor do seu salário?:R$'))
anos = int(input('Em quantos anos você pretende pagar o financiamento?: '))
prestação = casa / (anos * 12)
print(f'Posso pagar até no máximo R${salario * 30 / 100:.2f} por mês.')
print(f'O valor de sua parcela mensal é de:R${prestação:.2f}')
if prestação > salario * 30 / 100:
    print('Seu empréstimo foi NEGADO! A parcela mensal excede 30% do seu salário.')
else:
    print('Seu empréstimo foi APROVADO com sucesso!')