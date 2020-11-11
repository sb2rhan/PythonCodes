from hero import Hero
from player import Player
from random import randint
from logger import Logger
from datetime import datetime


names1 = ['Hoolan', 'Panther', 'Supra', 'Socko', 'Wolf']
names2 = ['Monster', 'Hamster', 'Wooba', 'Monlo', 'Stonk']

heroes1 = []
heroes2 = []
for i in range(len(names1)):
    heroes1.append(Hero(names1[i], randint(1000, 2500), randint(50, 250)))
    heroes2.append(Hero(names2[i], randint(1000, 2500), randint(50, 250)))


player1 = Player('Bob', heroes1)
player2 = Player('Mark', heroes2)

# Before battle
print(player1.__repr__())
print(player2.__repr__())

logger = Logger()
result = f'[{datetime.now()}]: {player1} vs {player2} : '
while True:
    if player1.start_game(player2) is False:
        result += (f'Winner - {player2}')
        break
    elif player2.start_game(player1) is False:
        result += (f'Winner - {player1}')
        break

print(result)
logger.write_logs(result)

# After battle
print(player1.__repr__())
print(player2.__repr__())
