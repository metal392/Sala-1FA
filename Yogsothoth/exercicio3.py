#escrever um programa que o usuario digita um numero de 1 a 20.
# O programa deverá fazer uma contagem regressiva;
#Não permitir que o usuario digita um numero maior que 20 ou menor que 1
# Imprimir uma mensagem de acabou a contagem no final
# Não permitir digitar letras

n = int(input("escreva um número de 1 a 20"))

if n > 20:
 print("número não aceito")

elif n < 1:
 print("número não aceito")

else:

 for i in range (n):
        print(n - i)

print("acabou a contagem")