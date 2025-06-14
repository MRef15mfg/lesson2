a = int(input("num 1 : "))
b = int(input("num 2 : "))
c = int(input("num 3 : "))
choice = input("Choose which action to use + or * : ")
if choice == "+":
    print(f"{a} + {b} + {c} = {a + b + c}")
elif choice == "*":
    print(f"{a} * {b} * {c} = {a * b * c}")
else:
    print("Error")