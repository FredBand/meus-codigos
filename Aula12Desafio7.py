# Refaça o desafio do triângulo, acrescentando o recurso de mostrar que tipo de triângulo será formado.
# Equilátero: todos os lados iguais, Isósceles: dois lados iguais, Escaleno: todos os lados diferentes.

seg1 = float(input('Qual o comprimento do primeiro segmento 1?: '))
seg2 = float(input('Qual o comprimento do segundo segmento 2?: '))
seg3 = float(input('Qual o comprimento do terceiro segmento 3?: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('Os segmentos acima podem formar um triângulo!')

    if seg1 == seg2 == seg3:
        tipo = "Equilátero"
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"

    print(f'Tipo de triângulo: {tipo}')
else:
    print('Os segmentos acima não podem formar um triângulo!')