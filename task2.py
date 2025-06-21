start = int(input("Введіть перше число: "))
end = int(input("Введіть друге число: "))

for number in range(start, end + 1):
    if number % 2 != 0:
        print(number)
