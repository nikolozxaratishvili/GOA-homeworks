# 1) ტემპერატურის შემოწმება
print("დავალება 1: ტემპერატურის შემოწმება")
temperature = float(input("შემოიტანე ტემპერატურა: "))

if temperature > 30:
    print("ძალიან ცხელა!")
elif temperature > 20:
    print("სასიამოვნო ამინდია")
elif temperature > 10:
    print("ცოტა ცივა")
elif temperature > 0:
    print("ცივა, ჩაიცვი თბილად")
else:
    print("გაიყინები, სახლში დარჩი!")


# 2) ქულისა და დასწრების შემოწმება
print("ქულისა და დასწრების შემოწმება")
score = int(input("შემოიტანე შენი ქულა: "))
attendance = int(input("შემოიტანე დასწრების პროცენტი: "))

if score > 80 and attendance > 90:
    print("შენ შესანიშნავად დაწერე გამოცდა")
elif score > 50 and attendance > 70:
    print("საშუალოდ დაწერე გამოცდა")
elif score > 30 or attendance > 50:
    print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა")
else:
    print("ჩაიჭერი!")


# 3) ამინდის შემოწმება (ტემპერატურა და წვიმა)
print("ამინდის შემოწმება")
temp = float(input("შემოიტანე ტემპერატურა: "))
rain = input("წვიმს? (შეიყვანე 'yes' ან 'no'): ").lower() # .lower() მომხმარებლის შეცდომებისგან თავის ასარიდებლად

if temp > 25 and rain == "no":
    print("შესანიშნავი ამინდია სასეირნოდ!")
elif temp > 25 and rain == "yes":
    print("ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!")
elif temp < 10 or rain == "yes":
    print("სჯობს სახლში დარჩე")
else:
    print("სასიამოვნო ამინდია")

# 4) ბილეთის ფასის შემოწმება
print("ბილეთის ფასის შემოწმება")
age = int(input("შემოიტანე შენი ასაკი: "))
student = input("ხარ თუ არა სტუდენტი? (შეიყვანე 'yes' ან 'no'): ").lower()

if age < 12 or age > 65:
    print("ბილეთი უფასოა")
elif student == "yes" and age > 12: # მოთხოვნის მიხედვით, 12 წლის სტუდენტი სრულ ფასს იხდის
    print("ბილეთი ნახევარ ფასად")
else:
    print("სრული ფასი უნდა გადაიხადო")

# 5) მომხმარებლის და პაროლის შემოწმება
print("მომხმარებლის და პაროლის შემოწმება")
username = input("შეიყვანე მომხმარებლის სახელი: ")
password = input("შეიყვანე პაროლი: ")

if username == "admin" and password == 'superSecretPassword':
    print("მოგესალმები, ადმინ!")
elif username == "guest" and password == "1234":
    print("მოგესალმები, სტუმარო!")
else:
    print("მომხმარებელი არ მოიძებნა!")
