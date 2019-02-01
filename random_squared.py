import random

for i in range(20):
    print(random.randint(0, 49))

random_numbers = [random.randint(0, 49) for i in range(20)]
print(random_numbers)

random_squared = [n*n for n in random_numbers]
print(random_squared)
