recipe = input()
# needs
B = recipe.count("B")
S = recipe.count("S")
C = recipe.count("C")

# stocked
B_S, S_S, C_S = [int(x) for x in input().split()]
# values
B_V, S_V, C_V = [int(x) for x in input().split()]

ruples = int(input())

# print(B,S,C)
# print(B_S, S_S, C_S)
# print(B_V, S_V, C_V)

count = 0
while ruples >= 0:
    curr_B, curr_S, curr_C = 0, 0, 0

    if B_S > 0:
        curr_B += min(B_S, B)
        B_S -= curr_B
    
    if S_S > 0:
        curr_S += min(S_S, S)
        S_S -= curr_S
    
    if C_S > 0:
        curr_C += min(C_S, C)
        C_S -= curr_C
    
    cost_of_missing_ingredients = (B - curr_B) * B_V + (S - curr_S) * S_V + (C - curr_C) * C_V
    ruples -= cost_of_missing_ingredients
    count += 1

    if B_S <= 0 and S_S <= 0 and C_S <= 0:
        break

if ruples < 0:
    print(count-1)
else:
    cost_of_burger = B * B_V + S * S_V + C * C_V
    count += ruples // cost_of_burger
    print(count)