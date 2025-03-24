import random
#1 - Selecione um valor aleatorio

list = [7,8,9,10,11,2]
print(random.choice(list))

#2 - Gera um numero aleatorio em uma intervalo de valores

r1 = random.randint(5,15)
print(r1)

#3- Seleciona caractere aleatoriro de uma string
name = "Curso de Python"
r2 = random.choice(name)
print(r2)

#4- Selecione mais de uma valor aleatorio

print(random.sample(list,2))