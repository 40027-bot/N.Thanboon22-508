# ข้อ 1 
def square(a):
    return a ** 2
print(square(4))

# ข้อ 2
def sum_of_squares(lst):
    total = 0
    for x in lst:
        total += x ** 2
    return total
print(sum_of_squares([1, 2, 3]))

# ข้อ 3
def concat_strings(str1, str2, str3):
    return str1 + str2 + str3
print(concat_strings("Hello", " ", "World"))

# ข้อ 4
def discounted_price(price, discount):
    return price - (price * discount / 100)
print(discounted_price(100, 10))

# ข้อ 5
def find_index(ls, k):
    for i in range(len(ls)):
        if ls[i] == k:
            return i
    return -1  
print(find_index([10, 20, 30, 40], 30))

# ข้อ 6
def month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if 1 <= month_number <= 12:
        return months[month_number - 1]
    else:
        return "Invalid month"
print(month_name(5))

# ข้อ 7
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum
print(find_min([5, 2, 9, 1, 7]))
