# TPC3

No ficheiro tpc3.ipynb, encontra-se a resolução do TPC3 proposto nesta Unidade Curricular.

A ficha permitiu consolidar obtidos na aula prática correspondente, nomeadamente extração de informações usando expressões regulares e a geração de documentos HTML.

A principal dificuldade encontrada foi lidar com quebras de página (ff), que interferiram na formatação correta do dicionário. Esta dificuldade foi ultrapassada utilizando a expressão "re.sub(r"(\f|\n\f)", "",texto)" que remove as quebras de página ou as ocorrências de nova linha seguidas por quebra de página do texto, resolvendo o problema.


No HTML, foram aplicadas melhorias na apresentação visual do conteúdo, nomeadamente,no tipo e cor da fonte, definição de margens modificação da cor de fundo e a utilização de elementos "div>" para organizar o conteúdo de forma mais estruturado.

Encontra-se abaixo um screenshoot do documento html melhorado:
![alt text](image.png)