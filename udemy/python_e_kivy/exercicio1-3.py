#coding: utf-8
# Na linha 1 é utilizado um comentário #coding: utf-8, que permite a acentuação.

# Faça um algoritmo que solicite o nome e a idade do usuário e então, envie a seguinte frase para o Console:
# "O seu nome é <nome> e a sua idade é <idade>".

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
#Na linha 8 o número digitado em string será convertido para um número inteiro.
print()
print("O seu nome é %s e sua idade é %i anos."%(nome,idade))



