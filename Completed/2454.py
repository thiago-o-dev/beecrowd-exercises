# 0 = vai pra direita
# 1 = vai pra esquerda

P, R = [bool(int(x)) for x in input().split()]

if not P:
    print("C")
elif R:
    print("A")
else:
    print("B")