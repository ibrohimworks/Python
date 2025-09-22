# 1. Age Calculator
name = input("Enter your name: ")
year = int(input("Enter your year of birth: "))
age = 2025 - year
print("Hello", name, "you are", age, "years old.")

# 2. Extract Car Names
txt1 = "LMaasleitbtui"
if "bmw" in txt1.lower():
    print("Found BMW")
if "tesla" in txt1.lower():
    print("Found Tesla")

# 3. Extract Car Names
txt2 = "MsaatmiazD"
if "mazda" in txt2.lower():
    print("Found Mazda")

# 4. Extract Residence Area
txt3 = "I'am John. I am from London"
words = txt3.split()
print("Residence area:", words[-1])

# 5. Reverse String
text = input("Enter a string: ")
print("Reversed:", text[::-1])

# 6. Count Vowels
word = input("Enter a word: ")
count = 0
for ch in word:
    if ch.lower() in "aeiou":
        count += 1
print("Vowels:", count)

# 7. Find Maximum Value
nums = input("Enter numbers separated by space: ")
nums_list = nums.split()
max_val = int(nums_list[0])
for n in nums_list:
    if int(n) > max_val:
        max_val = int(n)
print("Max value:", max_val)

# 8. Check Palindrome
w = input("Enter a word: ")
if w.lower() == w[::-1].lower():
    print("Palindrome")
else:
    print("Not palindrome")

# 9. Extract Email Domain
email = input("Enter your email: ")
parts = email.split("@")
print("Domain:", parts[1])

# 10. Generate Random Password (очень простой вариант)
import random
chars = "abc123!@#XYZ"
length = int(input("Password length: "))
password = ""
for i in range(length):
    password += random.choice(chars)
print("Password:", password)
