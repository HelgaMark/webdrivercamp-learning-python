#!/usr/bin/python3
import random

random_num = random.randint(-10, 10)
print(random_num)


if random_num < 0:
    print(random_num,"is negative")

elif random_num == 0:
    print(random_num,"is zero")

else:
    print(random_num, "is positive")

