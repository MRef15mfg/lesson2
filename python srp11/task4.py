balance = 1000

try:
    amount_str = input("Введіть суму для зняття: ")
    
    amount = float(amount_str)
    
    if amount % 10 != 0 or amount > balance:
        raise Exception("Некоректна сума для зняття")
    
    balance -= amount
    print(f"Ви зняли {amount}. Залишок на рахунку: {balance}")

except ValueError:
    print("Помилка: введено некоректне значення. Введіть число.")
except Exception as e:
    print(f"Помилка: {e}")

finally:
    print("Транзакція завершена")
