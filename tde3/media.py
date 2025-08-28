''' Peça ao usuário 3 notas, armazene em uma lista, e diga se a média é suficiente para aprovação (>=7). '''
notas = []
for i in range(3):
    nota = float(input(f'Digite a {i+1} nota: '))
    notas.append(nota)
media = sum(notas) / len(notas)
if media >= 7:
    print(f'Sua média é: {media:.2f}. Parabens foi aprovado!')
else:
    print(f'Sua média é {media:.2f}. Reprovado!')
