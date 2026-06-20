s = "Hello World"
#Slicing
s.upper()            # HELLO WORLD
s.lower()            # hello world
s.strip()            # removes extra spaces
s.replace("World", "Python")  # Hello Python
s.split(" ")         # ["Hello", "World"]
print(s.strip(s))
x = 6
y = 6

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif (x==y):
    print("x is equal to y")

#integers example
age = 17
score = 190
negative = -5

#float examples
gpa = 3.7
temperature = 99.6

#basic math
total = 10 + 5
difference = 10 - 3
product = 4 * 3
division = 10 / 3
whole_div = 10 // 3
remainder = 10 % 3
exponent = 10 ** 10
power = 2
# Built in math functions
print(abs(-10))
print(round(3.7))
print(round(3.14159, 2))
print(max(4, 9, 2))
print(min(4, 9, 2))
print(sum([1,2,3,4]))

#Extra for math
import math

print(math.sqrt(64))      # 8.0  — square root
print(math.pi)            # 3.14159... — value of pi
print(math.floor(3.9))    # 3    — round DOWN always
print(math.ceil(3.1))     # 4    — round UP always
print(math.factorial(5))  # 120  — 5! = 5×4×3×2×1
print(math.pow(2, 10))    # 1024.0 — same as 2**10 but returns float

#String is always in quotes

#Bool compare using <> ==

print (power > score )