import random
"""
random_integer = random.randint(1,10)
print(random)"""

random_number = random.random()
print(random_number)

"""
1. random.random() will return a random floating point number within the parameter range
2. random.uniform() will return a random floating point number a <= N <= b 
"""

#to get 0 and 100
random2 = random.random()*100
print(random2)

#to get 50 and 100
random3 = random.random() * 50 + 50
print(random3)

#a = (max-min) + min
min_value = 30
max_value = 110
scaled_value = random.random() * (max_value - min_value) + min_value
print(scaled_value)

#heads or tail
random4 =  random.randint(0,1)
if random4 == 0:
    print("Heads")
else:
    print("Tails")