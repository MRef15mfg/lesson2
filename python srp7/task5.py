text = input("Введіть текст: ")

if text:
    text = text[0].upper() + text[1:]

digits = 0
punctuation = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch in ".,!?:;-()\"'«»":
        punctuation += 1

print("Виправлений текст:", text)
print("Кількість цифр:", digits)
print("Кількість розділових знаків:", punctuation)
print("Кількість знаків оклику:", text.count('!'))
