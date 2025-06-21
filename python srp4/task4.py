N = int(input("Введіть кількість чисел: "))
max_num = 0
for i in range(N):
    num = float(input("Введіть число: "))
    if num > max_num:
        max_num = num

print("Максимальне число:", max_num)
