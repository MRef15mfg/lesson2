def print_even_numbers(start, end):
    if start > end:
        start, end = end, start
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num, end=' ')
    print()

print_even_numbers(12, 18)