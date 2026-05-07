
lst = [7, 8]
lst.append(9)
print("1)", lst)


data = []
for x in [3, 6, 9, 12, 15]:
    data.append(x)
print("2)", data)


fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print("3)", fruits)


print("4) remove შლის კონკრეტულ მნიშვნელობას, pop შლის ინდექსით (default ბოლო ელემენტს)")


nums = [11, 22, 33, 44]
last_item = nums.pop(-1)
print("5) ამოღებული:", last_item)
print("განახლებული:", nums)


arr = [10, 20, 40, 50]
middle = len(arr) // 2
arr.insert(middle, 30)
print("6)", arr)


values = [4, 1, 7, 2]
values.sort(reverse=True)
print("7)", values)


a = [5, 6, 7]
a.reverse()
print("8)", a)


names = ["gio", "nika", "dato"]
names.reverse()
print("9)", names)


items = [100, 200]
items.clear()
print("10)", items)


nums = [2, 4, 6, 8]
print("11)", nums.index(6))


words = ["sun", "moon", "star"]
user_input = input("12) სიტყვა: ")

if user_input in words:
    idx = words.index(user_input)
    print("ნაპოვნია ინდექსზე:", idx)
else:
    print("ვერ მოიძებნა")


numbers = []
for i in range(10):
    numbers.append(int(input("13) რიცხვი: ")))
print(numbers)


nums = []
for i in range(7):
    nums.append(int(input("14) რიცხვი: ")))

print("უდიდესი:", max(nums))
print("უმცირესი:", min(nums))


filtered = []
for i in range(10):
    n = int(input("15) რიცხვი: "))
    
    condition = (n > 0 and n % 2 == 0) or (n < 0 and n % 2 == 1)
    if condition:
        filtered.append(n)

if filtered:
    print("საშუალო:", sum(filtered) / len(filtered))
else:
    print("არცერთი შესაბამისი რიცხვი")