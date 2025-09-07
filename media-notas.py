def calcular_media_notas(alunos):
    # Soma todas as notas
    soma = sum(alunos.values())
    # Conta quantos alunos existem
    quantidade = len(alunos)
    # Calcula a média
    media = soma / quantidade if quantidade > 0 else 0
    # Retorna em formato de dicionário
    return {"média": media}