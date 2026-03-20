def foo() -> str: 
    N = int(input())

    C = []

    for i in range(N):
        C.append(int(input()))

    K = int(input())

    l, r = 0, len(C) - 1

    while l < r:
        curr = C[l] + C[r]

        if curr == K:
            return(f"{C[l]} {C[r]}")
        
        if curr < K:
            l += 1
        else:
            r -= 1

print(foo())
