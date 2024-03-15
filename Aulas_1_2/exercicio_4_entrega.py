# Importando biblioteca Math
import math

# Exercício 4)

# Escreva um programa em Python que calcule as duas
# raízes de uma equação de 2º grau ax²+bx+c, conhecendo os
# valores dos coeficientes da mesma (a, b, c). Suponha que as
# raízes são reais. Lembre-se que para calcular as duas raízes:

# Algoritmo: Preciso criar uma programa que use os valores de a, b e c
# para calcular os valores de delta, depois os valores de x1 e x2:

# Para isso devo usar as seguintes fórmulas:
# delta = (b*b) - 4*a*c
# x1 = -b + raiz(delta) / 2*a
# x2 = (-b - raiz(delta)) / 2*a

# Início do programa
print('Para calcular as raízes de uma equeção de segundo grau vou precisar dos seguintes dados:')

# Solicita os valores de a,b e c respectivamente
valorA = int(input('Digite o valor de A: '))
valorB = int(input('Digite o valor de B: '))
valorC = int(input('Digite o valor de C: '))

# Calcula o valor de Delta
delta = (valorB*valorB) - 4*valorA*valorC

# Calcula os valores de x1 e x2
valorX1 = (-valorB + (math.sqrt(delta))) / 2*valorA
valorX2 = (-valorB - (math.sqrt(delta))) / 2*valorA

# Imprime para o usuário
print('O valor de Delta é: %i' % (delta))
print('O valor de Delta é: %i' % (valorX1))
print('O valor de Delta é: %i' % (valorX2))
