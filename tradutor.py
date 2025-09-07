"""5. Tradutor Simples:
Desenvolva um programa que atue como um tradutor simples entre duas línguas. O
programa deve usar um dicionário onde as chaves são palavras em uma língua e os
valores são suas traduções em outra língua. O usuário deve poder fornecer uma
palavra como entrada e obter sua tradução como saída."""

dicionario = {
    "cachorro": "dog",
    "gato": "cat",
    "casa": "house",
    "carro": "car",
    "livro": "book",
    "mesa": "table",
    "cadeira": "chair",
    "janela": "window",
    "porta": "door",
    "computador": "computer",
    "telefone": "phone",
    "caneta": "pen",
    "lápis": "pencil",
    "papel": "paper",
    "escola": "school",
    "professor": "teacher",
    "aluno": "student",
    "cidade": "city",
    "país": "country",
    "mundo": "world",
    "sol": "sun",
    "lua": "moon",
    "estrela": "star",
    "água": "water",
    "fogo": "fire",
    "terra": "earth",
    "ar": "air",
    "comida": "food",
    "bebida": "drink",
    "fruta": "fruit",
    "legume": "vegetable",
    "carne": "meat",
    "peixe": "fish",
    "pão": "bread",
    "leite": "milk",
    "ovo": "egg",
    "azul": "blue",
    "vermelho": "red",
    "verde": "green",
    "amarelo": "yellow",
    "preto": "black",
    "branco": "white",
    "feliz": "happy",
    "triste": "sad",
    "rápido": "fast",
    "devagar": "slow",
    "grande": "big",
    "pequeno": "small",
    "novo": "new",
    "velho": "old"
}
palavra = input("Digite a palavra que você deseja traduzir: ").strip().lower()
traducao = dicionario.get(palavra)
if traducao is None:
    print("Desculpe, essa palavra não está no docionario.")
else:
    print(f"{palavra} em inglês é: {traducao}")