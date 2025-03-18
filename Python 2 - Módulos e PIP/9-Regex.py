import re

#1 - Indice inicial e final da palavra

text = "Onebitcode: Transformamos pessoas em programadores sem limites"

match = re.search(r'pessoas em programadores',text)
print(f"Indice inicial {match.start()}\nIndice final {match.end()}")

#2 - Buscando o indice que possui o ponto
site = 'https://onebitcode.com'
match = re.search(r'\.',site)
print(match)

#3 - Buscnado uma lista de caracteres dentro de uma frase
padrao = "[a-b]"
result = re.findall(padrao,text)
print(result)

#4 - Verificando o inicio de uma string
rule = r'^A'
phrase = ["A casa esta limpa", "O dia esta limpo"]
for f in phrase:
    if re.match(rule,f):
        print(f"Corresponde {f}")
    else:
        print(f"Nao corresponde {f}")
