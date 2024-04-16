from flask import Flask, render_template, request
import json
import os
app= Flask(__name__)

file=open(r"C:\Users\maryy\OneDrive\Ambiente de Trabalho\P. Linguagem Natural\pln-2324\TPC6\conceitoss.json","r", encoding='utf-8')
conceitos=json.load(file)


@app.route("/")

def home():
    return render_template("home.html")


@app.route("/conceitos")
def listarConceitos():
    return render_template("conceitos.html", conceitos=conceitos) # a variavel do jinja passa a ter o nome do load


@app.route("/conceitos/<designacao>")
def consultarConceitos(designacao):
    if designacao in conceitos:
        conceito_atual = conceitos[designacao]
        return render_template("descricoes.html", conceito=conceito_atual, designacao=designacao)
    else:
        return render_template("erro.html", erro="Conceito nao existe na nossa base de dados")

    
@app.route("/conceitos", methods=["POST"])
def adicionarConceitos():
    conceito= request.form.get("conceito")
    descricao=request.form.get("descricao")
    en= request.form.get("conceitEN")
    conceitos[conceito]={"desc": descricao,
                         "en":en}
    print(conceito,descricao,en)
    return render_template("conceitos.html", conceitos=conceitos)

@app.route("/conceitos/<designacao>", methods=["DELETE"])
def delete_conceito(designacao):
    os.rename("conceitoss.json","conceitos_backup.json")
    file_out=open("conceitoss.json","w")
    del conceitos[designacao]
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()
    return render_template("conceitos.html", conceitos=conceitos) 

@app.route("/pesquisa", methods=["GET"])
def pesquisa():
    palavra = request.args.get('palavra')
    if palavra is not None and palavra.strip(): 
        resultados = []
        for conceito in conceitos:
            descricao = conceitos[conceito]["desc"] 
            if palavra.lower() in conceito.lower() or palavra.lower() in descricao.lower():
                resultados.append({'conceito': conceito, 'descricao': descricao})
        return render_template("pesquisa.html", resultados=resultados, palavra=palavra)
    else:
        return render_template("pesquisa.html", resultados=[], palavra="")

    

@app.route("/table")
def table():
    return render_template("table.html",conceitos=conceitos)

app.run(host="localhost",port=4002,debug=True)