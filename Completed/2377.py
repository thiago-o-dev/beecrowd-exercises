L, D = [int(x) for x in input().split()]
K, P = [int(x) for x in input().split()]

print(K * L + (L // D) * P)