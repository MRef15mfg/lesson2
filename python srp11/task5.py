try:
    order_number = input("Введіть номер замовлення: ")
    
    if not (order_number.startswith("ORD") and order_number[3:].isdigit()):
        raise Exception("Неправильний формат номера замовлення")
    
    print(f"Номер замовлення '{order_number}' прийнято.")

except Exception as e:
    print(f"Помилка: {e}")

finally:
    print("Перевірка номера замовлення завершена")
