
with open("data.txt", "r") as file:
    content = file.read()
    encrypted = ""
    for char in content:
        if 'a' <= char <= 'y':
            encrypted += chr(ord(char) + 1)
        elif char == 'z':
            encrypted += 'a'
        elif 'A' <= char <= 'Y':
            encrypted += chr(ord(char) + 1)
        elif char == 'Z':
            encrypted += 'A'
        else:
            encrypted += char
    
    file.close()

with open("encrypted.txt", "w") as file:
    file.write(encrypted)
    file.close()