#coding: utf-8

# Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 >= n2:
    print("O maior número digitado é %i e o menor é %i" %(n1,n2))
else:
    print("O maior número digitado é %i e o menor é %i" % (n2, n1))