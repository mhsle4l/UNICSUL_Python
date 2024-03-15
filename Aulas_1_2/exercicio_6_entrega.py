# Exercício 6)
# Escreva um programa em Python que leia um valor
# representando o gasto realizado por um cliente do restaurante
# ComaBem e visualize o valor total a ser pago, considerando
# os 10% do garçom.

# Algoritmo: Receber o valor gasto pelo cliente, calcular o valor da conta mais
# os 10% do garçom e imprimir para o usuário.

# Inicio do programa
print('\nPara calcular o valor da sua conta, precisamos dos seguintes dados...')

# Preços por refeição no restaurante ComaBem
print('\n1 - Café da manhã -> R$ 50 por pessoa')
print('\n2 - Almoço -> R$ 80 por pessoa')
print('\n3 - Jantar -> R$ 100 por pessoa')

# Solicita o salário ao usuário
qntdPessoas = int(input('\nMesa para quantas pessoas? '))

# Mapeamento dos valores de entrada para os preços das refeições
refeicao_precos = {
    '1': 50.00,
    '2': 80.00,
    '3': 100.00
}

# Solicita qual o tipo de refeição o usuário optou
categoriaRefeicao = input('\nQual é a categoria da sua refeição? Digite o número correspondente: ')

# Transforma o que o usuário digitou em valor
preco_refeicao = refeicao_precos[categoriaRefeicao]

# Calculo para saber o valor do garçom
garcom = (qntdPessoas * preco_refeicao) * 0.10

# Preço da conta com o acréscimo do garçom
valorConta = (qntdPessoas * preco_refeicao) + garcom

# Imprime ao usuário
print(('\nO valor da sua conta é de: %.2f') % (valorConta))

# Fim :)
