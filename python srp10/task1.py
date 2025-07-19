def fun(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    summa = 1
    for i in range(min_num, max_num + 1):
        summa *= i
    return summa

print(fun(2, 5))