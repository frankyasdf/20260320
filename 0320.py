import random

lotto = [i for i in range(1, 43)]
random.shuffle(lotto)
print(lotto[:6])