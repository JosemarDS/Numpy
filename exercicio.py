import numpy as np
import matplotlib.pyplot as plt
import timeit 


# Desafio:
# 1. Crie um array de 20 elementos.
# 2. Extraia os primeiros 5 elementos, os últimos 5 elementos e os elementos 
# das posições 5 a 10.


indice = np.arange(0,20) # 1. Crie um array de 20 elementos.
print('Crie um array de 20 elementos:', indice)
percorrer = indice[15:] 
percorrer1 = indice[:5]
percorrer2 = indice[5:11]
print('Os últimos 5 elementos:', percorrer)
print("Os Primeiros 5 elementos:", percorrer1)
print('Os elementos das posições 5 a 10:', percorrer2)

# Desafio:
# 1. Crie duas matrizes 3x3.
# 2. Calcule o produto.


x = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
y = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]])


print(x)
print(y)
matriz = (x*y)
print(matriz)

a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
n= np.dot(x,y)

print(n)