def SumaCyfr(N):
    E = str(N)
    tablica = []
    for i in E:
        tablica.append(int(i))

    return sum(tablica)

print(SumaCyfr(7853))
