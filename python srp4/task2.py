usd = 39.2
eur = 41.5
pln = 9.6

while True:
    c = input("1: грн->валюта, 2: валюта->грн, 3: вихід: ")
    if c == '1':
        a = float(input("грн: "))
        v = input("1-USD,2-EUR,3-PLN: ")
        if v == '1': print(a/usd)
        elif v == '2': print(a/eur)
        elif v == '3': print(a/pln)
        else: print("невірна валюта")
    elif c == '2':
        v = input("1-USD,2-EUR,3-PLN: ")
        if v in ['1','2','3']:
            a = float(input("сума: "))
            if v == '1': print(a*usd)
            elif v == '2': print(a*eur)
            else: print(a*pln)
        else:
            print("невірна валюта")
    elif c == '3':
        break
    else:
        print("невірна опція")
