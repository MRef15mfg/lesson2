text = input("Введіть рядок: ")
search_word = input("Слово для пошуку: ")
replace_word = input("Слово для заміни: ")

new_text = text.replace(search_word, replace_word)

print("Результат:", new_text)
