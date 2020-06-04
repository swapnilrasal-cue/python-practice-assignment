import random

a = random.sample(range(100), 5)
b = random.sample(range(100), 7)

print(a)
print(b)

c = [ x for x in set(a) if x in b]
print(c)

