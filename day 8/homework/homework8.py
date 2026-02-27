#მონაცემთა ტიპები და თითოეულზე 5 ცვლადი

# int
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5

#float
b1 = 1.1
b2 = 2.2
b3 = 3.3
b4 = 4.4
b5 = 5.5

#string
c1 = "nika"
c2 = "school"
c3 = "python"
c4 = "hello"
c5 = "world"

#boolean
d1 = True
d2 = False
d3 = 5 > 3
d4 = 10 == 2
d5 = 7 != 4


#ოპერატორები

#არითმეტიკული ოპერატორები
print(5 + 3)
print(10 - 4)
print(6 * 2)
print(8 / 2)
print(10 % 3)

#შედარების ოპერატორები
print(5 > 3)
print(5 < 3)
print(5 == 5)
print(5 != 1)
print(7 >= 3)

#ლოგიკური ოპერატორები
print(True and False)
print(True or False)
print(not True)


#შედარების ოპერატორებზე 5 მაგალითი
print(10 > 5)
print(4 < 9)
print(6 == 6)
print(3 != 8)
print(15 >= 10)


#boolean მაგალითები
bool1 = True
bool2 = False
print(bool1)
print(bool2)


#ორი რიცხვი - პირველი მეტია თუ არა მეორეზე
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))
print(num1 > num2)


#პირველი > 10 და მეორე > 20
num3 = int(input("შეიყვანე პირველი რიცხვი: "))
num4 = int(input("შეიყვანე მეორე რიცხვი: "))
print(num3 > 10)
print(num4 > 20)


#რიცხვი 100-999 შუალედში
num5 = int(input("შეიყვანე რიცხვი: "))
print(100 <= num5 <= 999)