'''Um número perfeito é um número que é igual à soma de seus divisores,
excluindo ele mesmo. Crie um programa que verifique se um número
informado pelo usuário é perfeito.'''

num = int(input("Digite um número para verificar se é perfeito: "))
soma_divisores = 0

for i in range(1, num):
    if num % i == 0:
        soma_divisores += i

if soma_divisores == num:
    print(f"O número {num} é perfeito.")
else:
    print(f"O número {num} não é perfeito.")

print("Fim")