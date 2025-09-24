import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

num = 1
for i in range(1, 21):
    num = lcm(num, i)
print(num)
