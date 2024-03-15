# Exercício 1)
# Desenvolva um programa em Python que solicite ao
# usuário os valores dos lados de um retângulo e calcule e
# mostre seu perímetro e sua área.

# Algoritmo: Para calcular a área e o perímetro do triângulo preciso
# da fórmula, sendo elas: 

# - Área: base x altura / dois
# - Perímetro: somar todos os lados

# Inicio do programa
print('\nPara calcular o perímetro, precisamos dos seguintes dados...')

# Solicita os lados e a altura ao usuário
ladoA = int(input('\nInsira o valor do primeiro lado do triângulo: '))
ladoB = int(input('\nInsira o valor do segundo lado do triângulo: '))
ladoC = int(input('\nInsira o valor do terceiro lado do triângulo: '))

# Calcula o perímetro
perimetroTriangulo = ladoA + ladoB + ladoC

# Imprime para o usuário
print('\nO perímetro do triângulo é: ', perimetroTriangulo)

# Segunda parte do programa
print('\nPara calcular a área precisamos dos seguintes dados...')

# Solicita os valores para calcular a Altura
baseB = int(input('\nInsira o valor da base do triângulo: '))
alturaH = int(input('\nInsira o valor da altura do triângulo: '))

# Calcula a área
areaTriangulo = (baseB + alturaH) / 2

# Imprime para o usuário
print(('\nA área do triângulo é: %i') % (areaTriangulo))

# Fim :)