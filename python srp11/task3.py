try:
    input_str = input("Введіть оцінки студентів через пробіл: ")
    
    grades = list(map(float, input_str.split()))
    
    average = sum(grades) / len(grades)
    print(f"Середня оцінка: {average}")

except ValueError:
    print("Помилка: введено некоректне значення. Введіть лише числа.")
except ZeroDivisionError:
    print("Помилка: список оцінок порожній.")

finally:
    print("Завершення обчислень")
