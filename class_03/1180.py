n = int(input())
lista = []

for i in range (n):
    x = int(input())
    lista.append(x)
print(f'Menor valor: {min(lista)}')

for i in range (n):
    if lista[i] == min(lista):
        posicao = i
print(f'Posicao: {posicao}')
#PROBLEMA COM X = INT