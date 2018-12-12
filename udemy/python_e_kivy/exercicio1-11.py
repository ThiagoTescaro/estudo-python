#coding: utf-8

# Faça um algoritmo que solicite ao usuário digitar 2 números.
# Em seguida, imprima o total decimal da divisão e o total inteiro (sem casas decimais):

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segund número: "))

tdd = n1 / n2
tdi = n1 // n2

print("O total decimal da divisão entre %i e %i é %.2f. " %(n1, n2, tdd))
print("O total inteiro da divisão entre %i e %i é %.2f. " %(n1, n2, tdi))