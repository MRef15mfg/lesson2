text = input("Введіть текст: ")

words = text.split()
reversed_text = ""

for i in range(len(words) - 1, -1, -1):
    reversed_text += words[i] + " "

print("Зворотний текст:", reversed_text.strip())
