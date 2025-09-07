"""Estoque de Produtos:
Implemente um sistema simples de controle de estoque de produtos. O programa
deve permitir ao usuário adicionar novos produtos ao estoque, atualizar a
quantidade de produtos existentes e exibir o estoque atualizado. Use um dicionário
onde as chaves são os nomes dos produtos e os valores são as quantidades
disponíveis.
add novos produtos
atualizar quantidade
exibir estoque atualizado"""

produtos_supermercado = {
    "arroz": 5,
    "feijão": 3,
    "macarrão": 7,
    "óleo": 2,
    "açúcar": 4,
    "sal": 6,
    "leite": 10,
    "café": 8,
    "farinha": 2,
    "biscoito": 12
}

opcao = int(input(
    "Escolha uma opção:\n"
    "1 - Adicionar um novo Produto\n"
    "2 - Atualizar a Quantidade de um Produto Existente\n"
    "3 - Exibir o Estoque Atualizado\n"
))

match opcao:
    case 1:
        novo_produto = input("Digite o nome do novo produto: ").strip().lower()
        if novo_produto in produtos_supermercado:
            print("Esse produto já existe no estoque.")
        else:
            quantidade = int(input("Digite a quantidade do novo produto: "))
            produtos_supermercado[novo_produto] = quantidade
            print("Produto adicionado com sucesso.")

    case 2:
        produto_atualizar = input("Digite o nome do produto que deseja atualizar: ").strip().lower()
        if produto_atualizar not in produtos_supermercado:
            print("Esse produto não existe no estoque.")
        else:
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            produtos_supermercado[produto_atualizar] = nova_quantidade
            print("Quantidade atualizada com sucesso.")

    case 3:
        print(produtos_supermercado)
