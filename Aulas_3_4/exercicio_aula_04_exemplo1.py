# Exemplo 1 em aula - Vamos criar um programa que solicite ao usuário um número inteiro
# com três dígitos e exiba esse número com os dígitos invertidos.

# Solicita ao usuário um número para tirar a raiz
numero = int(input("\nDigite um número com três dígitos: "))

# Calcula o inverso do número atribuído a variável 'numero'
conta1 = numero // 100
conta2 = numero % 100 // 10
conta3 = numero % 10
inversoNumero = conta3*100+conta2*10+conta1

# Imprime para o usuário o número que ele forneceu e a raiz quadrada
print("\nO número que você digitou é esse %i e o inverso dele é: %i" %
      (numero, inversoNumero))

# Fim
