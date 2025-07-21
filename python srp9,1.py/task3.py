def print_square(size, symbol, filled):
    if filled:
        for i in range(size):
            print(symbol * size)
    else:
        for i in range(size):
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + ' ' * (size - 2) + symbol)

print_square(12, "*", True)