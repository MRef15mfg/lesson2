a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

start = min(a, b)
end = max(a, b)

total = 0
count = 0

for num in range(start, end + 1):
    total += num
    count += 1

average = total / count if count > 0 else 0

print("Сума чисел у діапазоні:", total)
print("Середнє арифметичне:", average)
