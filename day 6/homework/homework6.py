 #string, integer და float ცვლადები + ტიპები
name = "Nikolozi"
age = 14
height = 1.75

print(type(name))
print(type(age))
print(type(height))


#კილომეტრები მეტრებში
km = float(input("შეიყვანე მანძილი კილომეტრებში: "))
meters = km * 1000
print("მეტრებში:", meters)


#ორი რიცხვი და ყველა მათემატიკური ოპერაცია
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

print("მიმატება:", num1 + num2)
print("გამოკლება:", num1 - num2)
print("გამრავლება:", num1 * num2)
print("გაყოფა:", num1 / num2)


#BMI Calculator
weight = float(input("შეიყვანე წონა კილოგრამებში: "))
height = float(input("შეიყვანე სიმაღლე მეტრებში: "))

bmi = weight / (height * height)
print("შენი BMI არის:", bmi)

