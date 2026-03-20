A, G, R_A, R_G = [float(x) for x in input().split()]

res = "G"

if A/R_A < G/R_G:
    res = "A"

print(res)