

def leitura_arquivo(arquivo, qtd_linhas):
    with open(arquivo, "r", encoding="utf-8") as file:
        #I vira chave e line Valor (No caso da linha)
        for i, line in enumerate(file):
            if i >= qtd_linhas:
                break
            print(line.strip())
            
            
            

leitura_arquivo("Arquivos/names.txt", 3)