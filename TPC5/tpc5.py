import re
import json


file_traduzido=open(r'termos_traduzidos.txt','r',encoding='utf-8')
file_conceitos=open(r'conceitos.json','r', encoding='utf-8')
file_livro=open("LIVRO-Doenças-do-Aparelho-Digestivo.txt","r",encoding='utf-8')

termos_trad= file_traduzido.read()
conceitos=json.load(file_conceitos)
texto=file_livro.read()

# lista de tuplos
traduzidos= re.findall(r'(.+)\s@\s(.+)\n',termos_trad)

novo_dic={}

'''
#Nao cobre os conceitos que não têm termos traduzidos

for designacao in traduzidos:
    designacao_pt=designacao[0]
    designacao_en=designacao[1]
    if designacao_pt.lower() in conceitos:
       novo_dic[designacao_pt]={"desc": conceitos[designacao_pt], "en": designacao_en}
 '''

for designacao in conceitos: #dicionario
    for desig in traduzidos: # lista de tuplos
        if designacao in desig[0]:
            novo_dic[designacao]={"desc": conceitos[designacao], "en": desig[1]}
            break
            
        else:
            novo_dic[designacao]={"desc": conceitos[designacao]}
       
 
 # conceitos.json e termos_traduzidos.txt têm diferentes linhas, sugerindo que nem todos os conceitos do dic json estão traduzidos,
 # o que se comprovou depois de se fazer essa análise

file_out1=open("dic_trad.json","w",encoding='utf-8')
json.dump(novo_dic, file_out1,ensure_ascii=False, indent=4)
file_out1.close()


blacklist=['para', 'de', 'pelos', 'por', 'e', '[eE]ste','in']

def etiquetador(matched):
    palavra = matched[0]
    original = palavra
    palavra = palavra.lower()
    
    if palavra in novo_dic and palavra not in blacklist:
        if 'en' in novo_dic[palavra]:
            descricao = "Descrição: " + novo_dic[palavra]['desc'] + " Tradução (en): " + novo_dic[palavra]['en']
        else:
            descricao = "Descrição: " + novo_dic[palavra]['desc']
        etiqueta = f"<a href='' title='{descricao}'>{original}</a>"
        return etiqueta
    else:
        return original



expressao=r'[\wáçãêíúâ]+'
texto=re.sub(expressao, etiquetador, texto) #etiquetador recebe o que o padrao encontra commo uma lista
texto=re.sub(r'\n', '<br>', texto)
texto=re.sub(r'\f', '<hr>', texto)
file_out2=open("livro_trad.html", "w", encoding='utf-8')
file_out2.write(texto)
file_out2.close()