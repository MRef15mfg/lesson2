massive = [2, 3, 4, 5, 6, 7, 8, 9]
def fun(massive):
    summa = 0
    for i in range(len(massive)):
        summa = summa + massive[i]
    return summa
print(fun(massive))