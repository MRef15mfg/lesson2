import random

secret = random.randint(1, 500)
attempts = 0

while True:
    attempts += 1
    num = int(input("Введіть числo: "))
    if num < secret:
        print("Загадане число більше")
    elif num > secret:
        print("Загадане число менше")
    else:
        print("Правильно загадане число було : " + str(secret))
        print("Проб : " + str(attempts))
        break


    
