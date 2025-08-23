'''Crie um programa que gere a sequência de Fibonacci até o n-ésimo termo,
onde o primeiro e o segundo termo são 0 e 1, e os termos seguintes são a
soma dos dois termos anteriores.'''

n = int(input("Digite quantos termos da sequência de Fibonacci você quer ver: "))

# Verificação básica
if n <= 0:
    print("Por favor, insira um número positivo.")
elif n == 1:
    print("Sequência de Fibonacci: 0")
else:
    fib = [0, 1]
    while len(fib) < n:
        proximo = fib[-1] + fib[-2]
        fib.append(proximo)

    print("Sequência de Fibonacci:")
    print(" → ".join(str(num) for num in fib))