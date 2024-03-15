# Exemplo 5 em aula - A luz do sol, ao incidir num prédio, projeta uma sombra chão,
# formando um triângulo retângulo como o mostrado na figura
# abaixo. Faça um programa solicite o comprimento da sombra e o
# ângulo de inclinação dos raios solares, calcule e mostre a altura
# do prédio.

# Importação da biblioteca Math
import math as m

# Solicita ao usuário o comprimento da sombra em metros
sombra = float(input("\nDigite o valor do comprimento da sombra, em metros: "))

# Utiliza o método radians para descobrir o ângulo de inclinação entre a sombra e o prédio
angulo = m.radians(float(input("\nDigite um ângulo, em graus: ")))

# Calculo da altura utilizando os dados anteriores solicitados ao usuário
altura = m.tan(angulo) * (sombra)

# Imprime para o usuário o número que ele forneceu e a raiz quadrada
print("\nA altura do prédio é de %.2fm" % (altura))

# Fim
