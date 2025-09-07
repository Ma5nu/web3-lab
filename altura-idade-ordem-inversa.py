"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
ordem lida."""

idades = []
alturas = []
for i in range(5):
    idades.append(int(input(f"Digite a idade da pessoa {i+1}: ")))
    alturas.append(float(input(f"Digite a altura da pessoa {i+1} (em metros): ")))
idades.reverse()
alturas.reverse()
print(idades)
print(alturas)
    