numbers = input("Введіть числа через пробіл: ")
numbers = list(map(int, numbers.split()))
positive_sum = 0
for x in numbers:
    if x > 0:
        positive_sum += x
print("Сума додатних чисел:", positive_sum)
