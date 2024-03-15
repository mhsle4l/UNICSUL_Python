# 3 - Crie um programa em Python que solicite ao usuário a sua idade expressa em anos,
# meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias.
# Para isso considere 1 ano = 365 dias, 1 mês.

# Solicita ao usuário os valores do ano de nascimento, mes de nascimento
anoNascimento = int(input("\nDigite o ano que você nasceu: "))
# Instruções para o usuário, referente aos valores solicitados
print("\nInstrução para a próxima pergunta:")
print("Mês atual Abril(4) então mês anterior é igual a 3 (Março)")
mesAtual = int(input("Insira o mês anterior ao que você está: "))
diaMes = int(input("\nQual o dia do mês você está? "))

# Calcula quantos anos a pessoa tem
idadeEmAnos = 2024 - anoNascimento
# Calcula quantos dias ao total de vida a pessoa tem até o presente momento
idadeEmDias = (idadeEmAnos * 365) + (mesAtual * 30) + diaMes

# Imprime para o usuário o valor calculado
print("\nSua idade em dias é: %i" % (idadeEmDias))

# Fim
