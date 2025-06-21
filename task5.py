a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

start = min(a, b)
end = max(a, b)

print(f"Нормалізований діапазон: від {start} до {end}")

print("Непарні числа в діапазоні:")
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=' ')
