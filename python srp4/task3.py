start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

while True:
    num = int(input("Введіть число: "))
    if start <= num <= end:
        break
    print("Число поза діапазоном, спробуйте ще раз.")

for i in range(start, end + 1):
    if i == num:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")
