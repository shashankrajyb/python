#Display Using Constructor
class Sde:
    def __init__(self,no,name,sub):
        self.no = no
        self.name = name
        self.sub = sub
    def display(self):
        print('No', "=", self.no)
        print('name', '=', self.name)
        print('Subject', '=', self.sub)
s = Sde(567,"Raj","Ds")
q = Sde(1,'ramesh',"python")
q.display()
u = Sde(2,'suresh','django')
u.display()
o = Sde(3,'mahesh','ds')
o.display()
s.display()
#Display Using Object
class Student:
    def __init__(self,no,name,sub):
        print('No',"=",no)
        print('name','=',name)
        print('Subject','=',sub)
    def display(self,no,name,sub):
        print('no','=',no)
        print('name', '=', name)
        print('Subject', '=', sub)
q = Sde(1,'ramesh',"python")
q.display()

z = 40
class Info:
    y = 30
    print(z)
    def m1(self):
        self.y = 20
        print(self.y)
i = Info()
i.m1()
print(Info.y)

#Types of Methods
class TypesMethods:
    def __init__(self):
        print("in it method")
    def instance(self):
        print("Instance method")
    @classmethod
    def class_method(cls):
        print('Class method')
    @staticmethod
    def static_method():
        print('Static Method')


class Assignment:
    x = 10
    y = 20
    def method_one(self,x):
        self.z = 30
        print(Assignment.x)
        print(Assignment.y)
    @classmethod
    def method_two(cls,y):
      print(y)
      print(Assignment.x)
      print(Assignment.y)
a = Assignment()
a.method_one(50)
a.method_two(50)
