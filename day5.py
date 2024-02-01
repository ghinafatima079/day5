# Write a program that checks if a given number is positive, negative, or zero. 
# If it's positive, print "Positive number." If it's negative, print "Negative number." If it's zero, print "Zero."
num=int(input("Enter a number:"))
if num>0:
    print("Positive number.")
elif num<0:
    print("Negative number.")
else:
    print("Zero")
    
# Create a program that takes a student's exam score as input. Classify the student's performance
score=float(input("Enter your exam score:"))
if score>=90:
    print("A")
elif score>=80 and score<=89:
    print("B")
elif score>=70 and score<=79:
    print("C")
elif score>=50 and score<=69:
    print("D")
else:
    print("F")
    
# Write a program that determines whether a given year is a leap year or not.
# A leap year is either divisible by 4 but not divisible by 100, or it is divisible by 400.
year=int(input("Enter a year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
# Write a Python program that determines the price of a movie ticket based on the age and time of the show. 
# The program should take the age and time (in 24-hour format) as inputs
# use the match statement to calculate and print the ticket price
age=int(input("Enter your age:"))
time=int(input("Enter the time:"))
match age:
    case 0|1|2|3|4|5:
        cost=0
    case 6|7|8|9|10|11|12:
        cost=10
    case 13|14|15|16|17|18:
        cost=15
    case _:
        cost=20
if time>12:
    cost=cost-5
print(f"The cost of your ticket is {cost}")
    