with open("data.txt", "r") as file:
    lines = file.readlines()
    num_lines = len(lines)
print(f"Кількість рядків у файлі: {num_lines}")