import random as rand
import numpy as np

for i in range(11):
    print(rand.randint(0, 500)) # generates random number between 0 and 500

print('numpy random nums: {}'.format(np.random.randint(low=0, high=500, size=10)))