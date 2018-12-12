#coding: utf-8

#Faça um algoritmo em que o usuário informe uma medida em metros.
# Em seguida, converta essa medida para centímetros e envie para a saída padrão:

metros = float(input("Digite o valor em metros: "))
print("%.2f metro(s) equivale a %.2f centimetro(s)."%(metros, metros * 100))