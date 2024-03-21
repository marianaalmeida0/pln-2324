from flask import Flask, render_template
import json

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
    conceito_atual = conceitos[designacao]
    return render_template("descricoes.html", conceito=conceito_atual)

    
@app.route("/conceitos/<designacao>", methods=["PUT"])
def editarConceitos(designacao):
    return


  
app.run(host="localhost",port=4002,debug=True)