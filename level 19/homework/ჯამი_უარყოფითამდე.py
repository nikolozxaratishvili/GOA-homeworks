total = 0

while True:
    num = int(input("შეიყვანე რიცხვი: "))
    
    if num < 0:
        break  # გაჩერდი
    
    total += num

print("ჯამი:", total)