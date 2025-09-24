def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = 1000000
prime_sum = 0

for num in range(2, limit):
    if is_prime(num):
        prime_sum += num

print("Sum of primes below 1 million is:", prime_sum)
