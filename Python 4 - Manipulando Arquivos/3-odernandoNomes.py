
lista = []

with open("Arquivos/nomesPessoas.txt", "r", encoding="utf-8") as file:
    for line in file:
        nome = line.strip()
        if not nome:
            continue
        lista.append(nome)
    lista.sort()

with open("Arquivos/nomesPessoasOrdenado.txt", "w", encoding="utf-8") as file: 
    for nome in lista:
        file.write(f"{nome}\n")
    
        
