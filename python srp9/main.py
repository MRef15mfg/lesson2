def su(a, b, parm):
    summa = 0
    match parm:
        case "+":
            summa = a + b
        case "-":
            summa = a - b
        case "*":
            summa = a * b
        case "/":
            summa = a / b
    return summa


parts = input("Write (e.g. 5 + 3): ").split()

parts[0] = int(parts[0])
parts[2] = int(parts[2])

# print(parts)
print(su(parts[0], parts[2], parts[1]))
