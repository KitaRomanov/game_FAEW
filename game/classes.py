import random


class Dice:

    def __init__(self, name, *weakness):
        self.name = name
        self.weakness = [*weakness]

    def attack(self):
        if self.name == 'Fire' or self.name == 'Air':
            return random.randrange(0, 4, 1)
        else:
            return 1

    def defense(self):
        if self.name == 'Water' or self.name == 'Earth':
            return random.randrange(0, 4, 1)
        else:
            return 1


FireDice = Dice('Fire', 'Water')
WaterDice = Dice('Water', 'Earth', 'Air')
EarthDice = Dice('Earth', 'Air', 'Fire')
AirDice = Dice('Air', 'Fire')

dices = (FireDice, WaterDice, AirDice, EarthDice)
