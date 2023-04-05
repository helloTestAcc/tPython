#random.py

import random

print(random.random())
print(random.random())
print(random.uniform(1.0, 5.0))
print("--------randrange------")

print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

print("---------sample()---")
print(random.sample(range(20),10))
print(random.sample(range(20),10))
