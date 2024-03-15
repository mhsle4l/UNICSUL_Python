nomeAluno = input(str('\nQual o seu nome? '))
notaA1 = float(input('Quanto você tirou na A1? '))
notaA2 = float(input('Quanto você tirou na A2? '))

mediaSemestre = (notaA1 + notaA2) / 2

# Condicional composta para verificar se aluno está aprovado ou não
if mediaSemestre >= 6.0:
    print('\nAluno está aprovado!')
else:
    print('\nAluno está reprovado!')

# Forma de printar usando estrutura de dados como parâmetro
print(('\nA nota de %s na A1 é %.2f') % (nomeAluno, notaA1))
# Forma de printar igual em C
print(f'\nA nota de {nomeAluno} na A2 é {notaA2}')

# Forma de printar usando estrutura de dados como parâmetro
print(('\nA média de %s é %s') % (nomeAluno, mediaSemestre))
# Forma de printar igual em C
print(f'\nA média de {nomeAluno} é {mediaSemestre}\n')

# Fim :)