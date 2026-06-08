lower = 0
upper = 0

წინადადება = input("ჩაწერეთ რანდომ ტექსტი ")

for i in range(len(წინადადება)):

    if წინადადება[i].upper():
        upper = upper + 1

    elif წინადადება[i].lower():
        lower = lower + 1

print ("upper", upper, "lower", lower)