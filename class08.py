"""""
#List Comprehension
li = []
for i in range(0,101,2):
      li.append(i)
print(li)

li = [11,3,6,10,13]
for i in li:
    if i % 3 == 0:
        print(i ** 2)
for i in li:
    if i % 3 != 0:
        print(i ** 2)
for i in li:
    print(i +5)

#Word Score and Word weight
x = ['hi','python','we','write','python','we','say','hi','python']
y = {}
for i in x:
    if i in y.keys():
        y[i] = y[i] + 1
    else:
        y[i] = 1
print(y)

x = [('a',10),('b',20),('c',30),('d',40)]
for i in x:
        print(i[1],end = '')

x = ['a','b','c','d']
y = [10,20,30,40]
z = {}
for i in range (len(x)):
    z[x[i]] = y[i]
print(z)

x = ['a','b','c','d']
y = [10,20,30,40]
z = [(x[i], y[i]) for i in range(len(x))]
print(z)

#Types of Variables
x = 10
def f1():
    x = 20
    print(x)
    print(globals()['x'])
f1()
"""""

a = 10
b = 20
def f2():
    b = 30
    print(a)
    print(b)
    print(globals()['a'])
    print(globals()['b'])
f2()