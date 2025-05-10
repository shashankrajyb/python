"""
#To find factorial of a number
num = int(input('Enter the Number whose factorial has to be found : '))
fact = num
for i in range(1,num):
    fact = fact * i
print(f"factorial of the number is : {fact}")

#To find area of the Triangle
base = float(input('Enter the length of the base: '))
height = float(input('Enter the height of the triangle: '))
area = 0.5 * base * height
print(f"Area of the Triangle is{area}")

#To convert Miles into Kilometer
miles =float(input('Enter miles to covert into km: '))
kilometer = 1.6*miles
print(f"{miles} miles is converted into'{kilometer} kilometer")

#Calculate celsius to fahrenheit
celsius = float(input('Enter celsius to be converted: '))
fahrenheit = (celsius*9/5)+32
print(f"celsius is converted into {fahrenheit}")

#To display calender
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year,month)
print(cal)

#To swap two variable using a third variable
a = int(input("Enter first variable value: "))
b = int(input("Enter second variable value: "))
c = a
a = b
b = c
print(f"Swapped values: a={a},b={b}")

#Check wheather a number is postive,negative or zero
number = int(input("Enter the number: "))
if number > 0:
    print(f"The given number is positive {number}")
elif number == 0:
    print(f"Given number is zero {number}")
else:
    print(f"given number is negtive {number}")

#Multiplication of table
multiple = int(input("Enter the number for multiplication table: "))
for i in range(1,11):
        print(f"{multiple}X{i}={multiple * i}")
"""
#To print sum of numbers within a interval
