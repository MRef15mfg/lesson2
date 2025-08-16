try:
    input_str = input("Введіть послідовність чисел через пробіл: ")
    numbers = []
    
    for item in input_str.split():
        try:
            number = float(item)
            numbers.append(number)
        except ValueError:
            print(f"Попередження: '{item}' не є числом і буде пропущено.")
    
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"Сума чисел: {total}")
    print(f"Середнє значення: {average}")

except ZeroDivisionError:
    print("Помилка: список чисел порожній. Обчислити суму чи середнє неможливо.")

finally:
    print("Обробка даних завершена")
