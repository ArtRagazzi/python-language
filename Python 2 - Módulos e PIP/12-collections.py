from collections import Counter, namedtuple, deque
from operator import itemgetter

#1 - Contar items de uma Lista

fruits = ["Maça", "Cereja", "Abacaxi", "Banana", "Uva", "Abacaxi", "Uva", "Laranja"]

print(fruits)
print(Counter(fruits))

#2 - Utilizando tupla nomeada
game = namedtuple('game',['name','price','note'])

g1 = game("Fifa",90,8.5)
g2 = game("CS:2", 50, 10)

print(g1)
print(g2)

#3 - Ordenando Dicionarios
students = {"Pedro":20, "Ana":22, "Artur":23, "Jessica":12}
a = sorted(students.items(), key=itemgetter(0))
print(students)
print(a)

#4 - Utilizando fila ambas extremidades

deq = deque([20,40,60,90])
deq.appendleft(10)
print(deq)
deq.append(5)
print(deq)
deq.popleft()
deq.pop()
print(deq)