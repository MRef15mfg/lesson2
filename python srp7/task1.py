numbers = input("Введіть числа через пробіл: ")
numbers = list(map(int, numbers.split()))
print("Сума:", sum(numbers))
print("Середнє:", sum(numbers) / len(numbers))

