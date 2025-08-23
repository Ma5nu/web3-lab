'''10.Peça ao usuário para inserir dois números: um número base e um limite. Em
seguida, multiplique o número base por 1, 2, 3 até o limite e mostre a
tabuada.'''

base = int(input("Digite o número base da tabuada: "))
limite = int(input("Digite o limite da tabuada: "))

print(f"\nTabuada do {base} até {base} x {limite}:\n")

for i in range(1, limite + 1):
    resultado = base * i
    print(f"{base} x {i} = {resultado}")