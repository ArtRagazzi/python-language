

"""
w - write
a -append
r -read
"""

#Alternativa 1
#file = open("names.txt", 'a')
#file.write(f"{names}\n")
#file.close()

#Alternativa 2
for i in range(5):
    names = input("Digite Algo: \n")
    with open("Arquivos/names.txt", "a") as file:
        file.write(f"{names}\n")