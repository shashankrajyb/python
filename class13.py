
#Error Handling via try Except Block
li = [10,20,30,40,50]
x = 10
try:
    print(x/2)
    print(li[2])
    print(x/0)
except  Exception as e:
    print(e)


x = int(input('please enter the number: '))
print(x)
y = [10, 20, 30]
try:
      print(y[0])
      print(y[1])
      print(y[2])
      print(y[3])
except  Exception as e:
    print(e)

#Multiple Exception Handling
li = [10, 20, 30]
x = 10
try:
    print(x/0)
except  Exception as e:
    print(e)
try:
    print(li[2])
except  Exception as e:
    print(e)
try:
    print(x/0)
except  Exception as e:
    print(e)

#Named Exception
x = [10,20,30,40,50]
y = 10
try:
    print(x[0])
    print(y/0)
except IndexError:
    print('trying access a non exsistent element')
except ZeroDivisionError:
    print('Trying to divide number by zero')
except:
    print('An error occured')


#File Operation
#Write
f = open('sample.txt','w')
f.write('This is File Operation')
f.close()

#Append a new Text
f = open('sample.txt','a')
f.write('\nsay its not bad')
f.close()
#Read the Txt
f = open('sample.txt','r')
res = f.readlines()
print(res)

#Replace text in file
q = open('info.txt','w')
q.write('Bingo you won 999$')
q.close()
q = open('info.txt','a')
q.write('\n unknown msgs')
q.write('\ntrust unknown msgs')
q.close()
q = open('info.txt','a')
q.write('\nnot trust unknown msgs')
q.close()
q = open('info.txt','r')
lin = q.read()
content = lin.replace('not trust unknown msgs','Do not trust unknown msgs')
q.close()
q = open('info.txt','a')
q.write(content)
q.close()


j = open('example.txt','w')
j.write('This is file operation')
j.close()
j = open('example.txt','a')
j.write('\n we are creating a file')
j.close()
j = open('example.txt','r')
lin = j.read()
content = lin.replace('This is file operation','file I/O operation')
j.close()
j = open('example.txt','a')
j.write(content)
j.close()