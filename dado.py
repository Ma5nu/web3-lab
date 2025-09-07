"""Um dado é lançado 50 vezes, e o valor correspondente é armazenado em uma
lista. Faça um programa que determine o percentual de ocorrências de face 6 do
dado dentre esses 50 lançamentos.
quantas vezes o numero 6 aparece
qual o percentual de vezes que o numero 6 aparece"""

from random import randint

lancamentos = [randint(1, 6) for _ in range(50)]
seis = lancamentos.count(6)
percentual = (seis / 50) * 100

print(f"O número 6 apareceu {seis} vez(es) e o percentual de vezes que ele apareceu foi de {percentual:.2f}%.")