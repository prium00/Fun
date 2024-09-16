def loop():
    a = int(input("Enter your amount: "))
    b = str(input("Enter your sentence: "))
    c = 0

    while c < a:
        print(c + 1, ".", b)
        c += 1

loop()
