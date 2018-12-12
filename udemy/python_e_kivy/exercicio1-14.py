#coding: utf-8

# Faça um algoritmo que solicite ao usuário informar o valor de uma compra.
# Em seguida, aplique 10% de desconto e imprima na tela tanto o valor total e também o valor com o desconto aplicado.

valor_compra = float(input("Digite o valor da compra: "))

valor_desconto = valor_compra - (valor_compra * 0.10)
print()
print("valor Total: R$",valor_compra)
print("valor com 10% de dosconto: R$",valor_desconto)