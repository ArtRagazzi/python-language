
with open("Arquivos/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Estou aprendendo {line.rstrip()}")
        
    