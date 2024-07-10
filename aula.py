# Biblioteca Python
# Para desenvolvimento de estruturas compostas, suporta o processamento de grandes, 
# multi-dimensionais arranjos e matrizes, juntamente com uma grande coleção de 
# funções matemáticas de alto nível para operar sobre estas matrizes

import numpy as np
import matplotlib.pyplot as plt
import timeit

lista = ([1, 2, 3, 4, 5],[1, 2, 3, 4, 5])
array = np.array(lista)
print(array)
array_uns = np.ones(5)
print(array_uns)
array_zeros = np.zeros(5)
print(array_zeros)
array_sequencia = np.arange(10)
print(array_sequencia)
array_espacamento = np.arange(0, 10, 2)
print(array_espacamento)
array_espacado = np.linspace(1, 10)
print(array_espacado)
#7. Soma, subtração, multiplicação e divisão:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
print(soma, subtracao, multiplicacao, divisao)

#Calculos
vetor3 = np.array([1,11])
print(vetor3)

maior = np.max(vetor3)
menor = np.min(vetor3)
raiz = np.sqrt(vetor3)
media = np.mean(vetor3)
mediana = np.median(vetor3)
desvio_padrao = np.std(vetor3)
soma = np.sum(vetor3)
print(maior, menor, raiz, media, mediana, desvio_padrao, soma)

array_reshape = np.arange(6).reshape((2, 3))
print(array_reshape)

#Concatenação de arrays:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
concatenado = np.concatenate((a, b))
print(concatenado)

#Filtragem com condições:
condicao = array > 2
filtrado = array[condicao]  # Elementos maiores que 2
print(filtrado)

teste  = np.array([[1,2,3], [4,5,6], [7,8,9], [1,10,0]]) # 4x3
teste[3][1] = 20

print(teste.shape) # mostrar como a  matriz está estrutrada
print(teste.size)  # tamanho
print(teste.ndim)  # numero de dimensões - x e y

soma =  teste + teste

print(np.sum(teste))
print(np.min(teste))
print(np.max(teste))
print(np.std(teste))

numeros =  np.random.random()
numeros = np.random.randint(1,50)
numeros


#Desafio:
#1. Crie um array de 20 elementos.
#2. Extraia os primeiros 5 elementos, os últimos 5 elementos e os elementos 
#das posições 5 a 10.

#Desafio:
#1. Crie duas matrizes 3x3.
#2. Calcule o produto.


numeros =  np.random.random()
numeros = np.random.randint(1,50) # vetor aleatorio
numeros = np.random.randint(1,50, (5)) # com uma coluna de 5 numero
numeros = np.random.randint(1,50, (5,10)) # com 5 linhas 10 colunas
numeros = np.random.randint(1,50, (5,10,3)) # com 3 matriz 5 linhas 10 colunas,
                                                  


x =  np.array([1,11])
y =  np.array([1,11])
aleatorio1 =  np.random.randint(1,10,(5,10))
print('1:', aleatorio1)
aleatorio2 =  np.random.randint(1,10,(5,10))
print('2', aleatorio2)


