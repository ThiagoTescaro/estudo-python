#coding: utf-8

# Faça um algoritmo que peça a idade do usuário e a idade da sua mãe.
# Em seguida, imprima na tela com quantos anos sua mãe o teve.

idade_usuario = int(input("Digite sua idade: "))
idade_mãe = int(input("Digite a idade da sua mãe: "))

idade_mãe2 = idade_mãe - idade_usuario

print("Sua mãe te teve com %i anos." %idade_mãe2)