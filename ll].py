num = int(input('enter the number : '))
res = num
rev = 0
while num > 0 :
    rev = num % 10
    res = (rev % 10)+ rev
    num = num // 10
if rev == res:
   print(res,'is a palindrome number')
else:
    print(res,'is not a palindrome')
