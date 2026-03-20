import math

n = int(input())

j = math.isqrt(n) + 1
K = 0

for p in range(2, j):
    if n % p == 0:
        K += 1

        while n % p == 0:
            n //= p

if n > 1:
    K += 1

print(2 ** K - 1 - K)

