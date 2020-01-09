import random


class Dice:
    def roll(self):
        roll1 = random.randint(0, 6)
        roll2 = random.randint(0, 6)
        return roll1, roll2


fuzzy_dice = Dice()

print((fuzzy_dice.roll()))