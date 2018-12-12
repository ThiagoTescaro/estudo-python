#coding: utf-8

#Faça um algoritmo que leia dois números e imprima o maior.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 >= n2:
    print("O maior número digitado é %i" %n1)
else:
    print("O maior número digitado é %i" % n2)