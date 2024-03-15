# Exercício 5)
# Escreva um programa em Python que leia a cotação do
# dólar (taxa de conversão), leia um valor em dólares e converta
# e mostre o valor equivalente em Reais.

# Algoritmo: Solicita ao usuário quanto ele tem em dólar e depois imprime
# o valor em reais

# Inicio do programa
print('\nPara calcular o quanto vale seus dólares, precisamos dos seguintes dados...')

# Solicita o salário ao usuário
qntdDolar = float(input('\nInsira o valor que você possui em dólar: '))

# Preço do dólar
print('\nÚltimo valor do dólar no dia 02/03: US$ 1.00 = R$ 4.95')
cotacaoDolar = float(input('Qual a cotação do dólar hoje? (Se não souber, usar valor acima) '))

# Calcula o novo salário
valorEmReal = qntdDolar * cotacaoDolar

print(('\nSeu salário mais a comissão é de: %.2f') % (valorEmReal))

# Fim :)