hi, mi, hf, mf = [int(x) for x in input().split()]

ht = hf - hi
mt = mf - mi

if mt < 0:
    ht -= 1
    mt += 60

if ht == 0 and mt == 0:
    ht = 24

if ht < 0:
    ht += 24

print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")