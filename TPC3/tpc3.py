import re
f=open("dicionario_medico.txt",'r',encoding='utf-8')
texto=f.read()

# data clenaing
texto=re.sub(r"/f",'',texto)

#marcar designacoes
texto=re.sub(r"\n\n(.+)",r"\n\n@\1",texto)
texto=re.sub(r"@(.+)\n\n@",r"@\1\n",texto)

 #solucao para o FF

termos=[]
termos = re.findall(r'@(.+)\n([^@]+)',texto)
#print(termos)

# Gerar HTML
titulo = "<h1 style=\"text-align:center; color:blue; margin-top:50px; margin-bottom:20px;\">Dicionário Médico</h1>"
descricao = "<p style=\"text-align:center; margin-bottom:30px; font-size:18px;\">Este é um dicionário médico desenvolvido na unidade curricular PLEB</p>"
body = "<div style=\"margin-left:50px; margin-right:50px;\">"

for termo in termos:
    body += f"<div style=\"margin-bottom:30px; padding:15px; border:1px solid #ccc; border-radius:5px;\">"
    body += f"<h3 style=\"margin-bottom:10px; color:blue;\">{termo[0]}</h3>"
    body += f"<p style=\"margin-bottom:20px;\">{termo[1]}</p>"
    body += "</div>"

body += "</div>"

html = f"<html><head><style>body {{font-family: 'Garamond', serif; background-color:powderblue;}}</style></head><body>{titulo}{descricao}{body}</body></html>"

print(html)

file_out=open("dicionario_medico.html","w",encoding='utf-8')
file_out.write(html)
file_out.close()
