
print("Even or Odd Num")
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


print("Positive Or Nagetive")
num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



print("Largest No")
a, b, c = 10, 25, 15

if a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")


print("Leap Year Check")
year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



print("Vowel & Consonent")
ch = 'e'

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")



print("Divisible By :")
num = 55

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by both")





print("Prime Num Check")
num = 7

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")




print("Palindrom Num Check")
num = 121
rev = str(num)[::-1]

if str(num) == rev:
    print("Palindrome")
else:
    print("Not Palindrome")




print("Armstrong Program")
num = 153
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print("Armstrong")
else:
    print("Not Armstrong")




print("Marks No.")
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")



print("Day")
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
