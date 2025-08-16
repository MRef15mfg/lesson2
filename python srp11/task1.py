try:
    price = float(input("Введіть вихідну ціну товару: "))
    discount = float(input("Введіть відсоток знижки: "))

    final_price = price - (price * discount / 100)

    print(f"Фінальна ціна товару: {final_price} грн")

except ValueError:
    print("Помилка: введено некоректні дані. Введіть число.")

finally:
    print("Обчислення завершено.")
