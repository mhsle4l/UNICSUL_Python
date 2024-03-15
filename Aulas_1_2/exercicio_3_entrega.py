# Exercício 3)
# Escreva um programa em Python que solicite ao usuário a
# distância entre duas cidades e o tempo de viagem. O
# programa deverá calcular e exibir a velocidade média de um
# carro que vai de uma cidade para outra. Utilize a fórmula:

# Algoritmo: Receber o valor da distância e do tempo e fazer a distancia dividida
# pelo tempo e imprimir ao usuário.

# Inicio do programa
print('\nPara calcular a velocidade média até o seu destino, precisamos dos seguintes dados...')

# Solicita os dados ao usuário
distancia = int(input('\nInsira a distância entre as duas cidades, em km: '))
tempoViagem = int(input('\nInsira o tempo de viagem entre as duas cidades, em minutos: '))

# Conversão dos valores fornecidos pelo usuário
conversaoDistancia = distancia * 1000
conversaoTempo = tempoViagem * 60

# Calcula a velocidade média
velocidadeMedia = conversaoDistancia / conversaoTempo

# Imprime ao usuário a velocidade média de uma cidade até a outra
print(('\nA velocidade média é %.2f m/s') % (velocidadeMedia))

# Fim :)