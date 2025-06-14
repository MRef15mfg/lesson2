a = int(input("num 1 : "))
b = int(input("num 2 : "))
c = int(input("num 3 : "))

print("\nChoose an operation:")
print("1 - Find the maximum")
print("2 - Find the minimum")
print("3 - Find the average")

choice = input("Your choice: ")

if choice == "1":
    print("Maximum:", max(a, b, c))
elif choice == "2":
    print("Minimum:", min(a, b, c))
elif choice == "3":
    print("Average:", (a + b + c) / 3)
else:
    print("Invalid choice.")
