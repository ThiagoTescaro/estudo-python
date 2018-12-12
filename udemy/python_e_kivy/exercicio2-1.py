#coding: utf-8

#Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.

num = int(input("Digite um número: "))
print()
if num < 0:
    print("%i é um número negativo." %num)
elif num > 0:
    print("%i é um número positivo." % num)
else:
    print("Foi digitado o número 0.")
