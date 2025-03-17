def contador(texto):
    mai = 0
    min = 0
    for letra in texto:
        if(letra.isupper()):   
            mai+=1
        else:
            min+=1
            
    print("Maiuscula: ",mai)
    print("Minuscula: ",min)
    

def imparOuPar(lista):
    listaPar = []
    listaImpar = []
    for num in lista:
        if(num%2==0):
            listaPar.append(num)
        else:
            listaImpar.append(num)
    print(listaPar)
    print(listaImpar)
    
    
contador("Meu Texto Tem Muitas Letras")


    
imparOuPar([2,36,7,2,3,5,6,7,8,1,23])