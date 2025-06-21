while True:
    print("\nМеню:")
    print("1 — Знайти мінімум двох чисел")
    print("2 — Знайти максимум двох чисел")
    print("3 — Вихід")

    choice = input("Виберіть опцію (1, 2 або 3): ")

    if choice == "1":
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        print("Мінімум:", min(a, b))
    elif choice == "2":
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        print("Максимум:", max(a, b))
    elif choice == "3":
        print("Програма завершена.")
        break
    else:
        print("Некоректна опція. Спробуйте ще раз.")
