import random
import math

def roll_stat():
    rolls = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    rolls.sort()
    rolls.remove(rolls[0])
    return int(rolls[0] + rolls[1] + rolls[2])

roll_stat