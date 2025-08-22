'''Peça ao usuário para inserir um número e informe se ele é positivo, negativo
ou zero.'''

num = int(input('Digite um número: '))
print(f'O número {num} é positivo' if num > 0 else f'O número {num} é negativo' if num < 0 else f'O número é zero.')