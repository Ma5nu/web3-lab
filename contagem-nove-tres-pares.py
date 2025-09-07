"""3.Crie um programa que leia quatro valores pelo teclado e guarde-os em uma lista.
No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares."""

lista = []
pares = 0
nove = 0
primeiro_tres = None

for i in range(4):
    n = int(input(f"Digite o valor do {i+1}º numero: "))
    lista.append(n)
    if n == 9:
        nove +=1
    if n == 3 and primeiro_tres is None:
        primeiro_tres = i
    if n % 2 == 0:
        pares += 1
    
print(f"O valor 9 apareceu {nove} veze(s) na lista. O numero 3 apareceu pela primeira vez na posição {primeiro_tres}. Você digitou {pares} numeros pares")
print(lista)