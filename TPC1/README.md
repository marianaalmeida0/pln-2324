### Trabalho de casa 1
#### Identificação de anagramas
De forma a concretizar o trabalho de casa proposto, numa primeira etapa, procedeu-se à abertura e leitura do ficheiro de texto "CIH Bilingual Medical Glossary English-Spanish.txt", onde se especificou a codificação UTF-8 para garantir que os caracteres fossem lidos corretamente.

De seguida, efetuou-se um pré-processamento das palavras, de forma a normalizar o texto e facilitar a comparação de palavras. Assim, foi substituída alguma pontuação por um espaço em branco (".",",","-" e "/") e convertido o texto para minúsculas.

Posteriormente, foi divido o texto em tokens com recurso ao método split(), que cria uma lista de tokens. Para além disso, os tokens duplicados foram removidos, de forma a que cada palavra apenas apareça uma vez na lista.

Posto isto, procedeu-se para a etapa de identificação de anagramas. Para cada token na lista de tokens, os caracteres são ordenados alfabeticamente usando a função sorted() e, em seguida, juntados de volta para uma string usando o join(). Posteriormente, caso o token ordenado não exista nas chaves do dicionário de anagramas, é criada uma nova entrada onde a chave é o próprio token ordenado e o valor é uma lista com o token. Caso a chave exista, o token é adicionado à lista de valores que correspondem aquela chave.

Em suma, o código imprime o dicionário anagramas, que contém as chaves representando as sequências de caracteres ordenadas e os valores que contém as palavras que são anagramas umas das outras.
