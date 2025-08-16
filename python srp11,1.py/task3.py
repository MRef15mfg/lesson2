with open("data.txt", "w+") as file:
    file.write("Hello World")
    file.seek(0)
    data_read = file.read()
    file.close()

with open("backup.txt", "w+") as file:
    file.write(data_read)
    file.close()