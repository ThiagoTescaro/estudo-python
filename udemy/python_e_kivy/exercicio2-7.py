#coding: utf-8

# Faça um algoritmo que peça um número ao usuário e verifique se o mesmo é par ou então ímpar.
num = int(input("Digite um número: "))
print()
if num % 2 == 0:
    print("%i é um número par." %num)
else:
    print("%i é um número impar." % num)