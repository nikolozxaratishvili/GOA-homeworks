# 1) რა არის ფუნქცია? ახსენით საკუთარი სიტყვებით.
# ფუნქციით შეგვიძლია რაიმე კონკრეტული დავალება მარტივად შევასრულოთ

# 2) რატომ არის ფუნქციები საჭირო პროგრამირებაში? - ჩამოწერეთ მინიმუმ 3 მიზეზი
# ფუნქციები საჭიროა: კოდის მარტივად ხელახლა გამოყენებისთვის, კოდის წაკითხვის გასამარტივებლად და უფრო მოწესრიგებულია და სწრაფი

# 3) რა არის პარამეტრი (Parameter)?
# პარამეტრი არის ცვლადი რომელსაც ფუნქციის გასაკეთებლად ვიყენებთ

# 4) რა არის არგუმენტი (Argument)?
# რაიმე მნიშვნელობა რომელსაც ფუნქციას გადავცემთ გამოძახების დროს

# 5) რა განსხვავებაა პარამეტრსა და არგუმენტს შორის?
# პარამეტრი ცვლადია, არგუმენტი კი ამ ცვლადის მნიშვნელობა

# 6) შექმენით ფუნქცია repeat_word(word, count).
# - ფუნქციამ count-ჯერ უნდა დაბეჭდოს `word`
# - გამოიყენეთ for ციკლი
def repeat_word(word, count):
    for i in range(count):
        print(word)


def print_numbers(start, end):
    for i in range(start, end):
        print(i)


def count_even(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            count = count + 1
    print(count)

def count_vowels(text):
    count = 0
    vowels = "aeiou"
    for i in range(len(text)):
        if text[i].lower() in vowels:
            count = count + 1
    print(count)

def longest_word(words):
    if not words:
        return
    longest = words[0]
    for i in range(len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
    print(longest)

def filter_long_words(words, n):
    for i in range(len(words)):
        if len(words[i]) > n:
            print(words[i])


def name_lengths(names):
    for i in range(len(names)):
        print(names[i], len(names[i]))
names1 = input()
names = names1.split()
name_lengths(names)

def find_biggest(numbers):
    biggest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > biggest:
            biggest = numbers[i]
    print(biggest)

def find_min(numbers):
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    print(smallest)