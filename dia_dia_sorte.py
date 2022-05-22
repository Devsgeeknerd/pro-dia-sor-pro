# Módulos
from random import randint
from time import sleep

# Lista
lista = list()

# Jogos
jogos = list()

# Titulo
print('-' * 60)
print('        JOGANDO NO DIA DE SORTE        ')
print('-' * 60)

# Pergunta
quantidade =int(input('Quantos bilhetes você quer gerar? '))
total= 1

#Sorteando os números
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 31)
