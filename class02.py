#To find wheather the character is vowel or constant
character = input('enter the character :')
if character in 'a,e,i,o,u':
    print(character,'is a vowel')
else:
    print(character,'is a constant')
#Another solution for above
ch = input('enter the character :').lower()
if ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch =='u':
    print(ch,'is vowel')
else:
    print(ch,'is constant')
#To find wheather the given year is leap year or not`
year = int(input('enter the year value :'))
if year % 400 == 0 or year % 4 == 0 or year % 100 == 0:
    print(year,'is leap year')
else:
    print(year,'is not aleap year')
# cheack wheather it is palindraome or not
str = input('enter the keyword :')
if str == str [::-1]:
    print(str,'is a palindrome')
else:
    print(str,'is not a palindrome')
#find wheather rectangle or sqaure
length = input('enter the length :')
breadth = input('enter the breadth :')
if (length == breadth):
    print('it is square')
else:
    print('it is a rectangle')
#print the first 50 odd an evn number using loop
x = 2
while (x <= 100):
    print(x)
    x = x + 2
x = 1
while (x <= 99):
    print(x)
    x = x + 2
x = 2
while (x <= 65536):
    print(x)
    x = x * x
x = 3125
while ( x >= 5):
    print(x)
    x = x / 5
#print the first 50 odd an evn number using loop
x = 2
while (x <= 100):
    print(x)
    x = x + 2
x = 1
while (x <= 99):
    print(x,end = '')
    x = x + 2
x = 2
while (x <= 65536):
    print(x,end = '')
    x = x * x
x = 3125
while ( x >= 5):
    print(x,end = '')
    x = x // 5
x = 1
while x <= 10:
    print(f'1*(x) = (1 *x)')
    x = x + 1


