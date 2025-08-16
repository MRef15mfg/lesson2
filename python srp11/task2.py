try:
    dollars = float(input("Введіть суму в доларах: "))
    rate = float(input("Введіть курс обміну (долар → євро): "))

    if rate == 0:
        raise Exception("Курс обміну не може дорівнювати нулю")

    euros = dollars * rate
    print(f"Сума в євро: {euros} €")

except ValueError:
    print("Помилка: введено некоректні дані. Введіть число.")

except Exception as e:
    print(f"Помилка: {e}")

finally:
    print("Операцію завершено.")
