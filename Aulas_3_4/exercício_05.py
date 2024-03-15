# 5- Faça uma programa em Python que peça do usuário um valor em
# graus para um ângulo. Converta-o para radianos e, usando funções da
# biblioteca math, imprima o seno, cosseno e tangente deste ângulo.

# Importação da biblioteca Math
import math as m

# Utiliza o método radians para transformar os graus em radianos
angulo = m.radians(int(input("\nDigite um ângulo, em graus: ")))

# Calculo do seno, cosseno e tangente do valor recebido na variável 'angulo'
# através dos métodos math.sin(x), math.cos(x) e math.tan(x) da biblioteca Math
seno = m.sin(angulo)
cosseno = m.cos(angulo)
tangente = m.tan(angulo)

# Imprime para o usuário os valores do seno, cosseno e tangente
print("\nO seno do ângulo inserido é: %.2f" % (seno))
print("\nO cosseno do ângulo inserido é: %.2f" % (cosseno))
print("\nA tangente do ângulo inserido é: %.2f" % (tangente))

# Fim
