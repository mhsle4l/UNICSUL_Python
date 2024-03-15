# Exercício 2)
# Escreva um programa em Python que solicite ao usuário o
# salário atual e mostre o salário acrescido de 5% de comissão.

# Algoritmo: Receber o valor do salário, calcular os 5% e somar ao salário atual
# e imprimir para o usuário.

# Inicio do programa
print('\nPara calcular o salário acrescido de comissão, precisamos dos seguintes dados...')

# Solicita o salário ao usuário
salarioUsuario = float(input('\nInsira o valor do seu salário: '))

# Calculo da comissão
comissao = salarioUsuario * 0.05

# Calcula o novo salário
novoSalario = salarioUsuario + comissao

print(('\nSeu salário mais a comissão é de: %.2f') % (novoSalario))

# Fim :)
