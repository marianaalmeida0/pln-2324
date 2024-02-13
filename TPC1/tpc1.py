filename = "TPC1/CIH Bilingual Medical Glossary English-Spanish.txt"

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()
#file = open(filename)
#text = file.read()

# Remover pontuação
text = text.replace("."," ")
text = text.replace(","," ")
text = text.replace("-"," ")
text = text.replace("/"," ")
# ...

text = text.lower()

# Dividir o texto por tokens
anagramas = {}
tokens = text.split()

# remover repetidos
tokens = list(set(tokens))

# encontrar anagramas das chaves do dicionario; caso o token seja um anagrama, é adicionado aos valores do dic da respetiva chave
#tokens = ["sopa", "ola", "sapo"]
anagramas = {}
for token in tokens:
    # Ordenar os caracteres do token
    token_ordenado = ''.join(sorted(token))
    
    # Verificar se a chave já existe no dicionário
    if token_ordenado not in anagramas.keys():
        anagramas[token_ordenado] = [token]
    else:
        anagramas[token_ordenado].append(token)

print(anagramas)
