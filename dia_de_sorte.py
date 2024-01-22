# Importação de Módulos
from random import randint
from time import sleep

# Inicialização de Listas
lista = list()
# Jogos
jogos = list()

# Impressão do Título
print('-=' * 15)
print('         JOGO DIA DE SORTE         ')
print('-=' * 15)

# Entrada do Usuário
quantidade = int(input('Quantos bilhetes quer gerar? '))
total = 1

# Loop de Sorteio
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

# Impressão dos Jogos
print('-=' * 6, f' SORTEANDO {quantidade} JOGOS ', '-=' * 6)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

# Mensagem de Boa Sorte
print('-=' * 9, '< BOA SORTE!!! >', '-=' * 9)
