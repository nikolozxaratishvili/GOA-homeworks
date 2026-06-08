
word = "NIKA".lower()

word = word.lower()
print(word)


word = "example"
print(word.upper())


word = input("enter a word: ")
word = word.upper()
print(word)



word = "hello world".title()
print(word)


strings = ["nika", "football", "basketball", "bomboklat"]
for i in range(len(strings)):
    strings[i] = strings[i].title()
print(strings)

word = "My NAme IS NikA"
word = word.swapcase()
print(word)


word = "hello world"
print(word.count("l"))



sentence = input("enter random words: ")
symbol = input("enter a symbol ")
print(sentence.count(symbol))


name = input("Enter your name: ")
surname = input("Enter your surname: ")
print(name.title())
print(surname.title())



text = input("Enter a sentence: ")
text = text.lower()
vowels = "aeiou"
count = 0
for i in range(len(text)):
    if text[i] in vowels:
        count = count + 1

print(count)
