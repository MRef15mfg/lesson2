numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

s_neg = sum(x for x in numbers if x < 0)
s_even = sum(x for x in numbers if x % 2 == 0)
s_odd = sum(x for x in numbers if x % 2 != 0)

p_idx3 = 1
for i in range(0, len(numbers), 3):
    p_idx3 *= numbers[i]

a = numbers.index(min(numbers))
b = numbers.index(max(numbers))
x, y = sorted([a, b])
p_between = 1
if y - x > 1:
    for n in numbers[x+1:y]:
        p_between *= n
else:
    p_between = 0

pos = [i for i, x in enumerate(numbers) if x > 0]
s_between = sum(numbers[pos[0]+1:pos[-1]]) if len(pos) >= 2 else 0

print("Сума від'ємних чисел:", s_neg)
print("Сума парних чисел:", s_even)
print("Сума непарних чисел:", s_odd)
print("Добуток елементів з індексами кратними 3:", p_idx3)
print("Добуток між мінімальним і максимальним:", p_between)
print("Сума між першим і останнім додатними:", s_between)
