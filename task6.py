a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

start = min(a, b)
end = max(a, b)

print(f"Нормалізований діапазон: від {start} до {end}")

print("Парні числа у зростаючому порядку:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=' ')
print()

print("Непарні числа у спадному порядку:")
for num in range(end, start - 1, -1):
    if num % 2 != 0:
        print(num, end=' ')
print()
