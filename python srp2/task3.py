start = int(input("Введіть перше число: "))
end = int(input("Введіть друге число: "))

print("Парні числа в діапазоні (в спадному порядку):")


if start >= end:
    for number in range(start, end - 1, -1):
        if number % 2 == 0:
            print(number)


else:
    for number in range(end, start - 1, -1):
        if number % 2 == 0:
            print(number)
