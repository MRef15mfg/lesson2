with open("data.txt", "r") as file:
    content = file.read()
    num_lines = content.count("\n") + (1 if content else 0)
    num_words = len(content.split())
    num_chars = len(content)
    file.close()
    
with open("summary.txt", "w") as summary:
    summary.write(f"Рядки: {num_lines}\nСлова: {num_words}\nСимволи: {num_chars}\n")
    summary.close()