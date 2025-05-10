#Object & Class
"""
Class Details:
 x = 10
def m1(self):
     print('Hello')
d = Details
print(d.x)
d.m1()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your Location: ")
class PersonalDetails:
    def display_details(self,name,age,location):
        print("Name is",name)
        print("Age is",age)
        print("Location is",location)
p = PersonalDetails()
p.display_details(name, age, location)

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2: "))
class MathOperation:
    def sum(self,num1,num2):
        print("Sum = ",num1 + num2)
    def difference(self,num1,num2):
        print("Difference =",num1 - num2 )
    def product(self,num1,num2):
        print("product =",num1 * num2)
    def remainder(self,num1,num2):
        print("remainder =",num1 % num2)
k = MathOperation()
k.sum(num1,num2)
k.difference(num1,num2)
k.product(num1,num2)
k.remainder(num1,num2)

z = 30
class A:
    y = 20
    def m1(self):
        x = 10
        print(x)
        print(A.y)
print(z)
a = A()
a.m1()

class Student:
    def student_details(self,name,student_id):
        print(f"student name = {name},student id ={student_id}")
    def enrollment_details(self,enrollment id,enrollment_date):
        print(f"enrollment id = {enrollment id},enrollment date = {enrollment_date}")

class Info:
    def __init__(self,id,name,course):
          self.id = id
          self.name = name
          self.course = course
    def m1(self):
        print(self.id,self.name,self.course)
one = Info(31,"Raj","jst")
one.m1()
two = Info(346,"Ryan","Terrain")
two.m1()
three = Info(2345,"Naruto","Shadow Clone")
three.m1()
"""

class MathsOperation:
    def __init__(self,x,y):
           self.x = x
           self.y = y
    def sum(self):
            print(self.x + self.y)
    def difference(self):
            print(self.x  - self.y )
    def product(self):
            print(self.x * self.y )
    def division(self):
            print(self.x / self.y )
m = MathsOperation(5,6)
m.sum()
m.difference()
m.product()
m.division()