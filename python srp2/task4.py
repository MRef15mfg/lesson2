a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

order = int(input("Виберіть порядок (1 - зростання, 2 - спадання): "))

if order == 1:
    for i in range(min(a, b), max(a, b) + 1):
        print(i, end=' ')
elif order == 2:
    for i in range(max(a, b), min(a, b) - 1, -1):
        print(i, end=' ')
else:
    print("Некоректний вибір порядку.")
