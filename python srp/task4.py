meters = float(input("Введіть кількість метрів: "))

print("\nОберіть варіант:")
print("1 - Перевести в милі, дюйми або ярди")
print("2 - Перевести в милі, дюйми та ярди одразу")
print("3 - Перевести в кілометри та сантиметри")

choice = input("Ваш вибір: ")

if choice == "1":
    unit = input("Оберіть одиницю (mile / inch / yard): ").lower()
    if unit == "mile":
        print(f"{meters} м = {meters * 0.000621371} миль")
    elif unit == "inch":
        print(f"{meters} м = {meters * 39.3701} дюймів")
    elif unit == "yard":
        print(f"{meters} м = {meters * 1.09361} ярдів")
    else:
        print("Невірна одиниця.")


elif choice == "2":
    print(f"{meters} м = {meters * 0.000621371} миль")
    print(f"{meters} м = {meters * 39.3701} дюймів")
    print(f"{meters} м = {meters * 1.09361} ярдів")

elif choice == "3":
    print(f"{meters} м = {meters / 1000} км")
    print(f"{meters} м = {meters * 100} см")

else:
    print("Невірний вибір.")
