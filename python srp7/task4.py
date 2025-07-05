numbers = input("Введіть числа через пробіл: ")
numbers = list(map(int, numbers.split()))
even_indices = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indices.append(i)

print(even_indices)
