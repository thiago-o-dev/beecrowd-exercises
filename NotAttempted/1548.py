N = int(input())

for i in range(N):
    M_len = int(input())
    M_list = [int(x) for x in input().split()]

    new_sort = sorted(M_list, reverse=True)
    print(new_sort)