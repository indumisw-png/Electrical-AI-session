A = 1
B = 2
sum = 2
while A < 4000000 and B < 4000000:
    C = A + B
    if C % 2 == 0:
        sum = sum + C
    A = B
    B = C
print (sum)
