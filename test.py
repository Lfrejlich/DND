import dictionaries
import random
import statistics
import math


rolls = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
print(rolls)
rolls.sort()
print(rolls)
rolls.remove(rolls[0])
print(rolls)
x = int(math.ceil((rolls[0] + rolls[1] + rolls[2])/3))
print(x)