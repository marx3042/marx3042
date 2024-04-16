import numpy as np
import random

data1 = set(map(int, np.linspace(random.randint(1, 9999), 1000)))
data2 = set(map(int, np.linspace(random.randint(1, 9999), 1000)))

print(data1 & data2)

print(len(data1))