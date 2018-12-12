#coding: utf-8

# Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas, minutos e segundos.
# Em seguida, converta tudo para segundos:


# 1 minuto = 60 segundos
# 1 hora = 60 x 60 = 3600 segundos
# 1 dia = 24 x 3600 = 86400 segundos

dias = int(input("Digite o número de dias: "))
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de munutos: "))
segundos = int(input("Digite o número de segundos: "))
print()
total_de_segundos = ((dias * 86400) + (horas * 3600) + (minutos * 60) + (segundos))

print("Os valores digitados equivalem a %i segundos." %total_de_segundos)