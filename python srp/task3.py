
while True:
    grade = input("Введіть оцінку від 1 до 5: ")

    match grade:
        case "1":
            print("Дуже погано.")
        case "2":
            print("Погано.")
        case "3":
            print("Задовільно.")
        case "4":
            print("Добре.")
        case "5":
            print("Відмінно.")
        case _:
            print("Невірна оцінка. Введіть число від 1 до 5.")
