a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

print("\nОберіть операцію:")
print("1 - Додавання (+)")
print("2 - Віднімання (-)")
print("3 - Множення (*)")
print("4 - Ділення (/)")
print("5 - Залишок від ділення (%)")
print("6 - Піднесення до степеня (^)")

choice = input("Ваш вибір (1-6): ")
match choice:
    case "1":
        result = a + b
        op = "+"
    case "2":
        result = a - b
        op = "-"
    case "3":
        result = a * b
        op = "*"
    case "4":
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе!")
        result = a / b
        op = "/"
    case "5":
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе!")
        result = a % b
        op = "%"
    case "6":
        result = a ** b
        op = "^"
    case _:
        print("Невірний вибір операції.")
        exit()

print(f"\nРезультат: {a} {op} {b} = {result}")
