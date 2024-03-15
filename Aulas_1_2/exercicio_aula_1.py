# Impressão do nome do curso e da faculdade
print('\nAnálise e desenvolvimento de sistemas - Unicsul')

# Solicita a profissão da pessoa e imprime
profissao = input('\nDigite qual a sua profissão: ')
print('Eu sou um(a): ', profissao)

# Solicita a idade e imprime
idade = int(input('\nDigite a sua idade: '))
print('Sua idade é: ', idade)

# Solicita o sobrenome da pessoa e imprime
sobrenome = input('\nDigite o seu último sobrenome: ')
print('Família', sobrenome)

# Solicita o esporte favorito e imprime
esporte = input('\nDigite o seu esporte favorito: ')
print('Seu esporte favorito é: ', esporte)

# Imprime todo os dados recebidos
print('\nSua família é a %s, você é %s e tem %i anos e seu esporte favorito é o %s!' %
      (sobrenome, profissao, idade, esporte))

# Fim :)
