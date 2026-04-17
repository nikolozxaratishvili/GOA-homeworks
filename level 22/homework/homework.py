name = "Nikolozi"
print(name[0])

surname = "Xaratishvili"
print(surname[-1])

word = "Python"
print(word[2])

word2 = "Programming"
print(word2[:4])

word3 = "Computer"
print(word3[-3:])

word4 = "HelloWorld"
print(word4[3:7])

country = "Georgia"
print(country[2:6])

fav = "Apple"

if fav[0] == "A":
    print(fav[:3])
else:
    print(fav[-3:])

word5 = "Education"
print(word5[1:-1])

word6 = "Developer"
new_word = word6[:3] + word6[-3:]
print(new_word)

sentence = "I love programming"
print(sentence[:sentence.find(" ")])

letters = "abcdef"
print(letters[::2])

my_list = [1, "a", True, 3.14, "hello", 7, False, "end"]
print(my_list[2:6])

musicians = ["Eminem", "Drake", "Rihanna", "Adele", "Sia", "Bruno"]
print(musicians[-2:])