def inverterString(palavra):
    novaPalavra = ""
    for i in range(len(palavra)-1, -1, -1):
        novaPalavra+=palavra[i]
    return novaPalavra


def apenasPar(palavra):
    novaPalavra = ""
    for i in range(1,len(palavra),2):
        novaPalavra+=palavra[i]
    return novaPalavra

def apenasImpar(palavra):
    novaPalavra = ""
    for i in range(0,len(palavra),2):
        novaPalavra+=palavra[i]
    return novaPalavra
