#Single Inheritance
class A:
    def f1(self):
        print('class A,method - f1')
class B(A):
    def f2(self):
        print('class B,method - f2')
b = B()
b.f1()


#Multilevel Inheritance
class C:
    def m1(self):
        print('class c,method - m1')
class D(C):
    def m2(self):
        print('class D,method m2')
class E(D):
    def m3(self):
        print('class E,method m3')
e = E()
e.m1()
e.m2()
e.m3()


#Hierarchial Inheritance
class F():
    def f1(self):
        print('class F,method f1')
class G(F):
    def f2(self):
        print('class G,method f2')
class H(F):
    def f3(self):
        print('class h,method f3')
h = H()
h.f3()
g = G()
g.f1()


#multiple Inheritance
class I():
    def i1(self):
        print('class I,method i1')
class J():
    def i2(self):
        print('class J,method i2')
class K(I,J):
    def i3(self):
        print('class k,method i3')
k = K()
k.i2()


#Diamond Inheritance/hybrid Inheritance
class L():
    def i1(self):
        print('class I,method i1')
class M(L):
    def i2(self):
        print('class  J,method i2')
class N(L):
    def i4(self):
        print('class  n,method i4')
class O(M,N):
    def i3(self):
        print('class k,method i3')
o = O()
o.i1()
o.i2()


#Student Grading System
class Student():
    def __init__(self,Student_name,Student_roll_no,Subject_one,Subject_two,Subject_three):
         self.Student_name =  Student_name
         self.Student_roll_no = Student_roll_no
         self.Subject_one = Subject_one
         self.Subject_two = Subject_two
         self.Subject_three = Subject_three
    def average_marks(self):
            return (self.Subject_one + self.Subject_two + self.Subject_three) / 3
    def display_grade(self):
        average_marks = self.average_marks()
        if average_marks >= 90:
            grade = 'A'
        elif 75 <= average_marks < 90:
            grade = 'B'
        elif 50 <= average_marks < 75:
            grade = 'C'
        else:
            grade = 'D'

        print(f"Student: {self.Student_name}, Roll No: {self.Student_roll_no}, Average: {average_marks:.2f}, Grade: {grade}")
s1 = Student('Raj','5657',90,80,70)
s1.display_grade()


#Banking System
class BankAccount:
    def __init__(self, accountno, name, balance=0):
        self.accountno = accountno
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        damount = amount + self.balance
        print(f"balance is:{damount}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"New Balance: ₹{self.balance}")
    def display_balance(self):
        print(f"Current Balance:{self.balance}")
b = BankAccount(11576,'Raj',9999)
b.deposit(3000)
b.withdraw(5000)
b.display_balance()





