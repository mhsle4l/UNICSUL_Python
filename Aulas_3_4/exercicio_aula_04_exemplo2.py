# Exemplo 2 em aula - Vamos criar um programa que apresente o resultado da raiz quadrada
# de um número digitado pelo usuário. O programa em Python ficará
# assim:

# Importação da biblioteca Math
import math as m

# Solicita ao usuário um número para tirar a raiz
numero = float(input("Digite um número: "))
# Calcula a raiz quadrada do valor recebida pela variável 'numero'
resultado = m.sqrt(numero)

# Imprime para o usuário o número que ele forneceu e a raiz quadrada
print("A raiz quadrada de %.2f é: %.2f" % (numero, resultado))

# Fim
