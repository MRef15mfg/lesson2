text = input("Введіть рядок: ")
sym1 = input("Введіть перший символ: ")
sym2 = input("Введіть другий символ: ")

start = -1
end = -1

for i in range(len(text)):
    if text[i] == sym1 and start == -1:
        start = i
    elif text[i] == sym2 and start != -1:
        end = i
        break

if start != -1 and end != -1:
    new_text = text[:start] + text[end+1:]
else:
    new_text = text

print("Результат:", new_text)
