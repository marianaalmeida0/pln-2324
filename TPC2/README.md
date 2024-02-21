# TPC2

No ficheiro FICHA_RE_1.ipynb, encontra-se a resolução do TPC2 proposto nesta Unidade Curricular.

A ficha permitiu consolidar obtidos na aula prática correspondente, relativos às Expressões Regulares. Em Pyhton, para além dos conceitos básicos, foi necessário importar o módulo "re" para a utilização dos métodos "match","search", "findall", "sub" e "split".

Posto isto, foi elaborada a resolução de 10 exercícios propostos:

**Exercício 1**- Ao longo das alíneas, foram utilizados os métodos anteriormente referidos. Vale destacar que na alínea 1.3 foi usada a flag IGNORECASE para ignorar a escrita maiúscula e minúscula da palavra. Já na alínea 1.4, foi utilizada uma abordagem diferente, onde a frase foi transcrita em letras minúsculas e depois bastava substituir a palavra "hello" por *YEP* sem ser necessário flag.


**Exercício 2**- A inclusão das reticências com um sinal válido consituiu o maior desafio desta ficha. Depois de algumas tentativas, foi colocado a expressão regular r"por favor[\?\.\!\:\;]$|por favor\.{3}$", existindo assim duas possibilidades:
* A primeira parte do padrão (por favor[\?\.\!\:\;]$) procura por "por favor" seguido por um dos sinais de pontuação especificados (?, ., !, :, ;) no final da frase ($ indica o final da string).

* A segunda parte do padrão (por favor\.{3}$) procura por "por favor" seguido exatamente de três pontos (\.{3}) no final da frase.

**Exercício 3**- Para identificar exclusivamente a palavra "eu", foi utilizado o padrão '\beu\b' para encontrar apenas ocorrências da palavra completa. O método "findall" retorna uma lista de todas as ocorrências encontradas. Assim, para determinar quantas vezes a palavra aparece, basta contar o número de elementos nesta lista usando a função len(). Além disso, a flag 'IGNORE CASE' foi utilizada para garantir que a diferenciação entre maiúsculas e minúsculas seja ignorada durante a procura.

**Exercício 4**- Foi utilizado o método sub para substituir a palavra "LEI" por uma nova palavra.

**Exercício 5**- Uma vez que o resultado de "re.split((",",linha)" retorna uma lista com os números, bastou apenas utilizar um ciclo "for" para correr a lista e definir a variável "soma" que vai somando os elementos da lista.

**Exercício 6**- De forma a devolver todos os pronomes pessoais presentes numa determinada frase (ignorando os acentos e a escrita maiúscula e minúscula)foi usada a expressão regular r"\beu\b|\btu\b|\bel[ea]s*\b|\bn[oó]s\b|\bv[oó]s\b" para encontrar ocorrências dos pronomes "eu", "tu", "ele", "ela", "eles", "elas", "nós" e "vós", considerando que "ele" e "ela" podem ser representados pelo padrão el[ea]s*, que corresponde a "ele" ou "ela" seguido opcionalmente por "s" para indicar o plural.  Para o pronome "nós e vós" foi ainda possível encontrar estas palavaras sem acentos.De seguida, usou-se a função findall() para encontrar todas as ocorrências desses pronomes na frase, ignorando diferenças entre maiúsculas e minúsculas devido à flag re.IGNORECASE. 

**Exercício 7**- Inicialmente, utilizou-se a expressão regular ^[a-zA-Z] para garantir que a string comece com uma letra (maiúscula ou minúscula). Se a string não começar com uma letra, a função retorna False. De seguida, usou-se expressão regular ^\w*$ para garantir que a string contenha apenas letras, números ou underscores (_). Se a string conter qualquer outro caracter além desses, a função retornará False.

**Exercício 8**- Primeiramente,foi usado re.split(r",", string) para dividir a string em uma lista de números, utilizando a vírgula como delimitador.
De seguida, através do ciclo "for", é percorrido cada número na lista resultante e verifica-se se este contém um ponto decimal (representando um número real).Se o número contiver um ponto decimal,é ignorado e não é incluído na lista de inteiros.

**Exercício 9**- Foi usado e.sub() para substituir todas as ocorrências com um ou mais espaços em branco (\s+) na string por um único sublinhado (_).

**Exercício 10**-A função "codigos_postais(lista)" recebe uma lista de strings, onde cada string representa um código postal no formato "XXXX-XXX". Inicialmente, dividiu-se  cada código postal em duas partes, onde se separou o número antes e depois do hífen, utilizando a função re.split(r"-", cod).De seguida, cada parte foi armazenada como uma tuplo na lista "nova_lista". Assim, a função irá devolver uma lista de tuplos, onde cada tupla contém duas partes do código postal original, uma antes e outra depois do hífen. 
