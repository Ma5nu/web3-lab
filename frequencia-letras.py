"""Frequência de Letras:
Crie um programa que receba uma string como entrada e conte o número de
ocorrências de cada letra do alfabeto (ignorando maiúsculas/minúsculas). O

programa deve imprimir um dicionário onde as chaves são as letras do alfabeto e os
valores são o número de vezes que cada letra ocorre na string."""

letras ={}
frase = input("Digite uma frase: ").strip().lower()
for i in frase:
    if i.isalpha():
        letras[i] = letras.get(i, 0) + 1
print(letras)