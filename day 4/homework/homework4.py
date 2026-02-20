#Input ნიშნავს, რომ პროგრამაში შეგვყავს ინფორმაცია. ანუ მომხმარებელი რაღაცას წერს და პროგრამა ამას იღებს და ინახავს.

name = input("Enter your name: ")

#Output ნიშნავს, რომ პროგრამა გვიჩვენებს შედეგს ეკრანზე.

print("Hello")

#სახელის შეყვანა

name = input("Enter your name: ")
print("Hello " + name)

#ორი რიცხვის შეკრება

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print("Sum is:", number1 + number2)

#ასაკის გამოთვლა

birth_year = input("Enter birth year: ")
print("You are", 2026 - birth_year, "years old")

#საყვარელი ფილმი

movie = input("Enter your favorite movie: ")
print("Your favorite movie is " + movie)

#პაროლის შემოწმება

password = input("Enter password: ")
print("Your password is:", password)


#ცვლადი input-ით


name = "Nikolozi"
surname = "Xaratishvili"
address = "Agara"
hobby = "Computer and Football"
fav_movie = "Avatar"

print("My name is " + name + " " + surname + ". I live in " + address + ". My hobby is " + hobby + " and my favorite movie is " + fav_movie + ".")


#Case Sensitive Language

# Case Sensitive Language ნიშნავს,
# რომ პროგრამირების ენა არჩევს დიდ და პატარა ასოებს.

# მაგალითად Python-ში:
name = "Nika"
Name = "nika"

# ეს ორი ცვლადი განსხვავებულია, რადგან ერთი პატარა ასოთი იწყება, მეორე კი დიდი ასოთი.


# snake_case არის ცვლადებისა და სახელების დაწერის სტილი სადაც ყველა სიტყვა იწერება პატარა ასოებით და სიტყვები ერთმანეთისგან გამოყოფილია ქვედა ტირეთი (_) ეს სტილი ხშირად გამოიყენება Python-ში და კოდს უფრო წაკითხვადსა და გასაგებს ხდის.


# 1) ძაღლის სახელი და ტიპი
dog = input("Enter your dog's name: ")
print("Dog's name is " + dog)
print(type(dog))

# 2) ასაკის გამოთვლა
birth_year = int(input("Enter your birth year: "))
print("You are", 2025 - birth_year, "years old")
