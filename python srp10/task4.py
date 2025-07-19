def analyze_list(massive):
    paired = 0
    non_paired = 0
    plus = 0
    minus = 0

    for num in massive:
        if num % 2 == 0:
            paired += 1
        else:
            non_paired += 1
        if num > 0:
            plus += 1
        elif num < 0:
            minus += 1

    return paired, non_paired, plus, minus

massive = [-2, -3, -4, 2, 3, 4, 5, 6, 7, 8, 9]
result = analyze_list(massive)
print("Парних:", result[0])
print("Непарних:", result[1])
print("Додатних:", result[2])
print("Від’ємних:", result[3])
