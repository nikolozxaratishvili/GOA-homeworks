N = int(input("შეიყვანე რიცხვი: "))
count = 0

for i in range(1, N + 1):
    if i % 3 == 0:
        count += 1

print("პასუხი:", count)