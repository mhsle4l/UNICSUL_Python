# 4- Escreva um programa em Python para calcular o valor de uma
# prestação em atraso (prestacao). Para isso, obtenha o valor da
# prestação (valorPrestacao), a porcentagem de multa pelo atraso
# (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar
# o valor da prestação atualizado, sabendo que:

# prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

# Solicita os valores ao usuário da prestação, multa e quantidade de dias de atraso
valorPrestacao = float(
    input("\nQual o valor da sua prestação, em reais(R$)? "))
multa = float(input("\nQual o valor da multa por atraso, em porcentagem(%)? "))
qtdeDias = int(input("\nQuantos dias de atraso? "))

# Calcula o valor atualizado a prestação somando ao atraso atual
prestacaoEmAtraso = valorPrestacao + (valorPrestacao*(multa/100)*qtdeDias)

# Imprime para usuário o resultado
print("\nO valor da sua prestação atualizada com o atraso é de: %.2f" %
      prestacaoEmAtraso)

# Fim
