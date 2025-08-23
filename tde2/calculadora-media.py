'''Solicite ao usuário que informe três notas de um aluno e calcule a média. Em
seguida, informe se o aluno foi aprovado (média ≥ 7), reprovado (média < 5)
ou se está de recuperação (média entre 5 e 7).'''

sequencia = int(input('Informe o número de notas: '))
soma = 0
media = 0
notas = []
for i in range(sequencia):
    nota = float(input(f'Informe a nota {i + 1: } '))
    soma += nota

media = soma/sequencia
if media >= 7:
    print(f'O aluno foi aprovado com a média {media:.2f}.')
elif media < 5: 
    print(f'O aluno foi reprovado com média {media:.2f}')
else:
    print(f'O aluno está em recuperação com média {media:.2f}')
    

