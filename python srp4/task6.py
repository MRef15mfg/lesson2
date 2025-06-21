shape = input("1 : Квадрат чи 2 : прямокутник? ").lower()
if shape == "1":
    size = int(input("Довжина сторони: "))
    char = input("Символ: ")
    for i in range(size):
        print(char * size)

elif shape == "2":
    width = int(input("Ширина: "))
    height = int(input("Висота: "))
    char = input("Символ: ")
    for i in range(height):
        print(char * width)
