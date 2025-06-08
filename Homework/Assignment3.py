# 1) Write a program to check entered character is vowel or not.
# x = input("Enter any character :")
# if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
#     print("Given Character is Vowel.")
# else:
#     print("Given Character is Not Vowel.")

# 2) Write a program to print weekday if entered day number is 1,2,3,4,5 & print
# if entered day is 6 or 7 & invalid day if value not between 1 and 7.

# x = int(input("Enter Number :"))
# if x == 1:
#     print("Monday")
# elif x == 2:
#     print("Tuesday")
# elif x == 3:
#     print("Wednesday")
# elif x == 4:
#     print("Thursday")
# elif x == 5:
#     print("Friday")
# elif x == 6:
#     print("Saturday")
# elif x == 7:
#     print("Sunday")
# else :
#     print("Invalid Input.")

# 3)Write a program to find greatest among three numbers .
# x = int(input("Enter First Number :"))
# y = int(input("Enter Second Number :"))
# z = int(input("Enter Third Number :"))
#
# if x >= y and x >= z:
#     print("Greatest Number Is :", x)
# elif y >= x and y >= z:
#     print("Greatest Number Is :", y)
# else:
#     print("Greatest Number Is :", z)

# 4) A candidate is recruited based on following criteria : if male , age should be above 30 yrs
#  and height above 160. If female ,age should be above 25 yrs and height should be above 155.
gen = input("Enter Gender :")
gender = gen.upper()
age = int(input("Enter Age :"))
h = int(input("Enter Height :"))

if gender == 'MALE' and age >= 30 and h >= 160:
    print("Candidate is Recruited .")

elif gender == 'FEMALE' and age >= 25 and h >= 155:
    print("Candidate is Recruited .")

else:
    print("Candidate is Not recruited .")