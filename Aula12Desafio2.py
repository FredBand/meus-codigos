# Escreva um programa que leia uma número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão: 1 - para binário, 2 - para octal e 3 - para hexadecimal.

num = int(input('Digite um número inteiro qualquer: '))
print('Escolha uma das bases de conversão:')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')

escolha = input('Escolha de 1 a 3 para definir a base de conversão: ')
print(f'Você escolheu: {escolha}')

if escolha == "1":
    print(f'{num} convertido para binário é: {bin(num)[2:]}')
elif escolha == "2":
    print(f'{num} convertido para octal é: {oct(num)[2:]}')
elif escolha == "3":
    print(f'{num} convertido para hexadecimal é: {hex(num)[2:].upper()}')
else:
    print('Opção inválida!')
