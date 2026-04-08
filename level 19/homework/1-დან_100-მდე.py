for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        print("EvenFive")
    elif i % 2 == 0:
        print("Even")
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)