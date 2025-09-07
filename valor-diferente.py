"""Faça um programa que preencha por leitura uma lista de 10 posições, e conta
quantos valores diferentes existem na lista."""

lista = []
b = 0

for i in range(10):
    n = int(input(f"Digite o valor numero {i+1}: "))
    if n not in lista:
        b += 1
print(f"Você digitou {b} valores diferentes")