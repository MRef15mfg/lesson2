text = input("Введіть рядок: ")

cleaned = ''
for char in text:
    if char.isalnum():
        cleaned += char.lower()

is_palindrome = True
for i in range(len(cleaned) // 2):
    if cleaned[i] != cleaned[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Це паліндром.")
else:
    print("Це не паліндром.")
