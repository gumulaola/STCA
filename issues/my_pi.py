import math
from random import random

n = 1000000
hit = 0
for i in range(n):
    x = random()
    y = random()
    lens = math.sqrt(x**2 + y**2)
    if lens <= 1:
        hit += 1
print(4*(hit/n))
