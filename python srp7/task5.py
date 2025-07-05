numbers = input("Введіть числа через пробіл: ")
numbers = list(map(int, numbers.split()))
result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(result)
