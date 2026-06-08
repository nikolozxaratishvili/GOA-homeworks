
text = " hello world "
text = text.strip()

name = input("enter a name with spaces")
print(name.strip())

word = input("enter a random word: ")
print(word.startswith("A"))

website = input("enter a website address")
print(website.startswith("https"))

file = input("Enter file name: ")
print(file.endswith(".py"))


email = input("enter your email: ")
print(email.endswith("@gmail.com"))



text = text.replace("jemala", "nugzara")
print(text)

text = input("enter a sentence: ")
text = text.replace(" ", "-")
print(text)

number = input("Enter phone number: ")
number = number.replace("-", "")
print(number)




text = input("Enter text: ")
text = text.strip()

print(text.startswith("Hello"))



password = input("Enter password: ")
print(password[0] in "QAZWSXEDCRFVTGBYHNUJMIKOLP")

print(password.endswith("1"))


text = input("Enter a sentence: ")
text = text.strip()
text = text.replace(" ", "_")
if text.endswith("."):
    print(text)
else:
    text = text + "."
    print(text)



fullname = input("enter you name, lastname, and father's name: ")
fullname = fullname.split()
print(fullname[0])
print(fullname[1])
print(fullname[2])

print(len(fullname))


sentence = input("enter a sentence: ")
words = sentence.split()
longest = words[0]
shortest = words[0]
for i in range(len(words)):
    if len(words[i]) > len(longest):
        longest = words[i]
    if len(words[i]) < len(shortest):
        shortest = words[i]
print(longest)
print(shortest)