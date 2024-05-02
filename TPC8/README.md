# **TPC8**
## Word Embeddings

## Objetivos:
O objetivo deste trabalho de casa foi a exploração e avaliação de modelos Word2Vec treinados com uma combinação de textos dos livros "Harry Potter e a Pedra Filosofal" e "Harry Potter e a Câmara Secreta". Desta forma, pretende-se explorar o desempenho de diferentes modelos Word2Vec, através da configuração de hiperparâmetros e posteriormente,avaliar e comparar esses modelos com base na capacidade de capturar a semelhança de palavras, analogias, palavras "intrusas", entre outras.

## Procedimento:

1. Combinação de textos dos ficheiros txt `Harry_Potter_Camara_Secreta-br.txt` e `Harry_Potter_e_A_Pedra_Filosofal.txt`.

2. Configuração dos hiperparâmetros do modelo `Word2Vec`, dando origem a 3 modelos diferentes.

3. Avaliação do melhor modelo com  base no método `most_similar("harry")`.

4. Realização dos diferentes testes: **similiaridade de palavras**, **similiaridades entre pares de palavras**, **analogias** e **palavra "intrusa"**.


## Testes e Análise dos Resultados Obtidos

Após a combinação dos dois textos presentes nos ficheiros referidos, procedeu-se à configuração dos hiperparâmetros do modelo `Word2Vec`, de forma a avaliar qual teria um melhor desempenho. Através do método `most_similar()`, averigou-se que o melhor modelo seria o modelo 1, com os hiperparâmetros vector_size=100, window=5, min_count=1, sg=1, epochs=5, workers=3, uma vez que ao avaliar palavras similiares a "harry", o modelo conseguia retornar resultados que faziam sentido (nomes de personagens). Em contrapartida, os restantes modelos não retornavam resultados válidos.
Com efeito, para a realização de testes adicionais, foi utilizado o modelo 1.

Foram realizados os seguintes testes: 

1. **Similiaridade entre palavras**\
        - &#x25B6; "harry"\
        - &#x25B6; "potter"\
        - &#x25B6; "sonserina"\
        - &#x25B6; "voldemort"

2. **Similaridade entre pares de palavras**\
        - &#x25B6; "harry", "magia",\
        - &#x25B6; "hermione","snape",\
        - &#x25B6; "grifinória", "sonserina" \
        - &#x25B6; "dursley" ,"grunnings"   
Resultados: 
    | Palavra 1   | Palavra 2   | Similaridade |
    |-------------|-------------|--------------|
    | harry       | magia       | 0.69         |
    | hermione    | snape       | 0.84         |
    | grifinória  | sonserina   | 0.97         |
    | dursley     | grunnings   | 0.79         |



3. **Palavra "intrusa"**\
        - &#x25B6; "filho", "tia", "cozinha"\
        - &#x25B6; "rony", harry, "dumbledore"\
        - &#x25B6; "granger", "hermione", "rony"\
        - &#x25B6; "grifinória", "hermione", "sonserina"
Resultados: 
    | "Intruso" Esperado |"Intruso" Identificado |
    |-----------------------------|---------------------------------|
    | cozinha                        | filho                        |
    | dumbledore                       | harry                      |
    | granger                     | granger                            |
    | hermione                  | hermione                       |

4. **Analogias** \
        - &#x25B6; "harry", "hermione", "rony"\
        - &#x25B6; "draco", "sonserina", "hermione"\
        - &#x25B6; "harry", "gryffindor" , "snape"\
        - &#x25B6; "draco", "mione", "sonserina"  
        - &#x25B6; "draco", "malfoy", "hermione"
    | Analogia                                       | Resultado Obtido|
    |-----------------------------------------------|--------------------|
    | harry : hermione :: rony : ???               | mione             |
    | draco : sonserina :: hermione : ???          | magia            |
    | harry : grifinória :: snape : ???            | parasse          |
    | draco : mione :: sonserina : ???             | hermione          |
    | draco : malfoy :: hermione : ???             | diário           |

## Conclusão

Após a realização dos testes, é possível verificar que o modelo não está a ter o desempenho ideal. Desta forma, para um melhor desempenho, seria necessário nova configuraçãodos hiperparâmetros do modelo.