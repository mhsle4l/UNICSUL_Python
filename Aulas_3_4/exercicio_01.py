# 1 - Faça um programa em Python que calcule e mostre o valor do volume
# do tronco de uma pirâmide, para isso o programa deve solicitar ao
# usuário os valores da altura do tronco da pirâmide (h), o valor da
# base menor (Bmenor) e o da base maior (Bmaior) ecalcular a seguinte
# expressão:
# volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

# Solicita ao usuário os valores da altura(h), Base menor(Bmenor), Base maior(Bmaior)
altura = float(input("Insira o valor da altura do tronco de uma pirâmide: "))
Bmenor = float(
    input("Insira o valor da base menor do tronco de uma pirâmide: "))
Bmaior = float(
    input("Insira o valor da base maior do tronco de uma pirâmide: "))

# Realiza o calculo do volume do tronco de uma pirâmide
volume = altura/3 * (Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2) ** 0.5)

# Imprime para o usuário o valor do volume calculado
print("O valor do volume do tronco da pirêmide é: %.2f" % (volume))
