import math

def fun(massive):
    result = []
    for num in massive:
        if num < 0:
            result.append(None) 
        else:
            result.append(math.factorial(num))
    return result

massive = [-2, -3, -4, 2, 3, 4, 5, 6, 7, 8, 9]
print(fun(massive))
