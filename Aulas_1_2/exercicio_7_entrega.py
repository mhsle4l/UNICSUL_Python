# Exercício 7)

# Escreva um programa em Python que obtenha uma
# temperatura em graus Celsius, calcule e mostre a respectiva
# temperatura nas escalas Fahrenheit e Kelvin. Utilize as
# fórmulas abaixo:

# Algoritmo: Receber os valores em Celsius e calcular baseado nas fórmulas
# tF = 1,8 * tC + 32
# tK = tC + 273
# E devolver ao usuário.

# Inicio do programa
print('\nPara te informar a temperatura em Farenheit e Kelvin, precisamos dos seguintes dados...')

# Solicita a temperatura ao usuário em Celsius
tCelsius = int(
    input('\nDigite a temperatura, em Celsius, na sua cidade hoje: '))

# Calculo para descobrir a temperatura em Farenheit e Kelvin
tFarenheit = (1.8 * tCelsius) + 32
tKelvin = tCelsius + 273

# Imprime ao usuário as temperaturas em Farenheit e Kelvin
print('\nA temperatura da sua cidade em Farenheit é %iF' % (tFarenheit))
print('\nE a temperatura da sua cidade em Kelvin é %iK' % (tKelvin))

# Fim :)
