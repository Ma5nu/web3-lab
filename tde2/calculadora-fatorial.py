#Crie um programa que leia um número e calcule o fatorial desse número. O
#fatorial de um número é o produto de todos os números inteiros de 1 até ele.

num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial do número {num} é {fatorial}.")