# To find biggest and smallest numbers in list
from os import remove

li = [9,4,6,7,2]
biggest = 0
smallest = 0
for i in li:
    if (i > biggest):
        biggest = i
print(biggest,' is biggest number in the list',)
if (i < smallest):
    smallest = i
print(i,'is smallest number in the list',)

di = {
'houseno':int(input('enter h.no : ')),
'street':input('enter your street name : '),
'city':input('enter your city name : '),
'pincode':input('enter your pincode : ')
        }
for i,j in di.items():
    print(i,'=',j)
####
li = []
for i in range(5):
    num = int(input('enter the number: '))
    li.append(num)
    print(li)

num = int(input('enter the number : '))
res = num
rev = 0
while num > 0 :
    rev = num % 10
    rev = (rev % 10)+ rev
    num = num // 10
    if rev == res:
        print(res,'is a palindrome number')
    else:
     print(res,'is not a palindrome')