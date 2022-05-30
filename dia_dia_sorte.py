# Módulos
from random import randint
from time import sleep

# Lista
lista = list()

# Jogos
jogos = list()

# Titulo
print('-=' * 15)
print('         JOGO DIA DE SORTE         ')
print('-=' * 15)

# Pergunta quantos jogos serão gerados
quantidade = int(input('Quantos bilhetes quer gerar? '))
total = 1

# Sorteio
while total <= quantidade:
    contagem = 0
    while True:
        numero = randint(1, 31)
        if numero not in lista:
            lista.append(numero)
            contagem += 1
        if contagem >= 7:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 6, f' SORTEANDO {quantidade} JOGOS ', '-=' * 6)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
