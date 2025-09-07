'''Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado(entre 0 e 20) e mostrá-la por extenso.'''

numeros_por_extenso = (
    "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

n = int(input("Digite um numero de 1 até 20: "))

for i in range(0, 21):
    if n == i:
        print(f"Você digitou o numero {numeros_por_extenso[i-1]}")
        break