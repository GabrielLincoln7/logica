

from random import randint

print("Jogo de Dados")

dados1 = randint(1, 6)
dados2 = randint(1, 6)
jogador1 = dados1 + dados2

dados3 = randint(1, 6)
dados4 = randint(1, 6)
jogador2 = dados3 + dados4

print("dados 1:", dados1)
print("dados 2:", dados2)
print("dados 3:", dados3)
print("dados 4:", dados4)   

print("Jogador1 ", jogador1)
print("Jogador2 ", jogador2)

if jogador1 > jogador2:
     print("Jogador 1 venceu!!!")
if jogador2 > jogador1:
     print("Jogador 2 venceu!!!")
else:
     print("Empate!")
