import hashlib

# 1- Verificar os algoritmos disponiveis

print(hashlib.algorithms_available)

# 2- Verificar os algoritmos disponiveis para o SO

print(hashlib.algorithms_guaranteed)

#3 - Utilizando o sha256
algoritmo = hashlib.sha256()
print(algoritmo.digest())

menssagem = "A melhor forma de prever o futuro e cria-lo".encode()
algoritmo.update(menssagem)
print(algoritmo.hexdigest())

#4- md5
md5 = hashlib.md5()
md5.update(menssagem)
print(md5.hexdigest())