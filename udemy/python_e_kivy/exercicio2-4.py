#coding: utf-8

# Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou então,
# se a mesma é de menor.

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade.")
else:
    print("Maior de idade.")