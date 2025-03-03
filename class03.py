li = [10,20,13,61,50]
for i in range (0,len (li),2):
    print(' element in odd indices :',li[i],end = '')
for i in range (1,len(li),2):
    print(' element in even indices :',li[i],end = '')
for i in range (1,len(li),2):
    print(li[i],end = '')
print('/n')
for i in li:
    if i % 2 == 0:
        print(i,'is an even element')
    else:
        print(i,'is a odd element')
print('/n')
sum = 0
for i in li:
    sum = sum + i
print('sum of elements is',sum)
print('sum of odd and even elements')
sum_even = 0
sum_odd = 0
for i in li:
    if 1 % 2 == 0:
        sum_even = sum_even + 1
    else:
        sum_odd = sum_odd + 1
print('sum of even number is ',sum_even)
print('sum of odd numbers is',sum_odd)
print('sum of odd and even indices')

str = input("Enter a character: ")
word_count = 0
space_count = 0
for i in range(len(str)):
    if str[i] == ' ':
        space_count = 1
    elif i == 0 or str[i - 1] == ' ':
        word_count += 1
print("Number of words:", word_count)
print("Number of spaces:",space_count)
 st = input('enter the string')
 space_count = 0
 word_count = 0
 for i in st:
     if 1 == '':
         space_count = space_count + 1

vow = input("Enter the string: ").lower()
vowels = ('a', 'e', 'i', 'o', 'u')
for i in vow:
    if i in vowels:
        print(f"'(i)' is a vowel")
    else:
        print(f"'(i)' is not a vowel"


