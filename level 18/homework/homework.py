# 1) 200 დან 500 მდე -> 4-ის და 7-ის საერთო ჯერადები

# For ციკლი
for i in range(200, 501):
    if i % 4 == 0 and i % 7 == 0:
        print("საერთო ჯერადი (for):", i)

# While ციკლი
i = 200
while i <= 500:
    if i % 4 == 0 and i % 7 == 0:
        print("საერთო ჯერადი (while):", i)
    i += 1


# 2) 300 დან 1000 მდე -> 3-ის ან 10-ის ჯერადები

# For ციკლი
for i in range(300, 1001):
    if i % 3 == 0 or i % 10 == 0:
        print("ჯერადი (for):", i)

# While ციკლი
i = 300
while i <= 1000:
    if i % 3 == 0 or i % 10 == 0:
        print("ჯერადი (while):", i)
    i += 1


# 3) 1 დან 50 მდე Even / Odd

for i in range(1, 51):
    if i % 2 == 0:
        print("ლუწი:", i)
    else:
        print("კენტი:", i)


# 4) მომხმარებელი შეიყვანს 10 რიცხვს

positive = 0
negative = 0

for i in range(10):
    num = int(input("შეიყვანე რიცხვი: "))
    
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("დადებითი რიცხვების რაოდენობა:", positive)
print("უარყოფითი რიცხვების რაოდენობა:", negative)


# 5) შემოწმება 2-ზე და 3-ზე გაყოფის

num = int(input("შეიყვანე რიცხვი: "))

if num % 2 == 0 and num % 3 == 0:
    print("კარგია")
elif num % 2 == 0:
    print("მხოლოდ 2-ზე იყოფა")
elif num % 3 == 0:
    print("მხოლოდ 3-ზე იყოფა")
else:
    print("არცერთზე არ იყოფა")


# 6) FizzBuzz (1 დან 100)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# 7) სანამ 0 არ შეიყვანს

positive = 0
negative = 0

while True:
    num = int(input("შეიყვანე რიცხვი (0 გასასვლელად): "))
    
    if num == 0:
        break  # ციკლიდან გასვლა
    elif num > 0:
        positive += 1
    else:
        negative += 1

print("დადებითი რიცხვები:", positive)
print("უარყოფითი რიცხვები:", negative)


# 8) 1 დან n მდე (4-ზე გამოტოვება)

n = int(input("შეიყვანე რიცხვი: "))

for i in range(1, n + 1):
    if i % 4 == 0:
        # თუ იყოფა 4-ზე -> გამოვტოვოთ
        continue
    print(i)


# 9) 5 რიცხვი (Even / Odd)

# For ციკლი
for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    
    if num % 2 == 0:
        print("ლუწი")
    else:
        print("კენტი")

# While ციკლი
count = 0

while count < 5:
    num = int(input("შეიყვანე რიცხვი: "))
    
    if num % 2 == 0:
        print("ლუწი")
    else:
        print("კენტი")
    
    count += 1