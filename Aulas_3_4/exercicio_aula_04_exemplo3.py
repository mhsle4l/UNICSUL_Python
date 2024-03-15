# Exemplo 3 em aula - Vamos criar um programa solicite um número real, calcule e que
# apresente: a) o valor absoluto; b) somente sua parte inteira; c) sua raiz
# quadrada; d) o fatorial desse número.

# Importação da biblioteca Math
import math as m

# Solicita ao usuário um número para tirar a raiz
numero = float(input("Digite um número real: "))

# Calcula o valor absoluto do valor recebida pela variável 'numero'
absoluto = m.fabs(numero)
# Calcula o valor inteiro do valor recebida pela variável 'numero'
inteiro = m.trunc(numero)
# Calcula a raiz quadrada do valor recebida pela variável 'numero'
resultado = m.sqrt(numero)
# Calcula o fatorial do valor recebida pela variável 'numero'
fatorial = m.factorial(inteiro)

# Imprime para o usuário o número que ele forneceu e a raiz quadrada
print("A raiz quadrada de %.2f é: %.2f" % (numero, resultado))

# Fim
