M, N = [int(x) for x in input().split()]

people_total = [0] * N
changed = []

for i in range(M):
    X, value, Y = [int(x) for x in input().split()]
    if X not in changed:
        changed.append(X)
    if Y not in changed:
        changed.append(Y)


    people_total[X-1] -= value
    people_total[Y-1] += value

if len(changed) < M:
    print("S")
else:
    print("N")

print(max(people_total), min(people_total))