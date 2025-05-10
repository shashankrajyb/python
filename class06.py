# #To print index of the tuple
# tu =(1,2,3)
# ele = int(input('Enter the element whose index has to be determined: '))
# if ele in tu:
#     print('The index of',ele,'is',tu.index(ele))
# else:
#     print(ele,'is not present in tuple')
# #To add items in set
# s = set()
# print('Enter the numbers:')
# for i in range(5):
#     num = int(input())
#     s.add(num)
#     print(s)
# s2 = {12, 13, 14, 15, 16, 17}
# ele = int(input('Enter the element to be deleted: '))
# if ele in s2:
#     s2.remove(ele)
#     print("Updated set s2:", s2)
# else:
#     print(ele, 'is not present in set s2')
#Adding items to empty dictionary
di = {}
name = input('Enter your name: ')
email = input('Enter your Email: ')
city = input('Enter your city: ')
mobile = int(input('enter your mobile number: '))
pin =int(input('Enter your pin: '))
di['name'] = name
di['email'] = email
di['city'] = city
di['mobile'] = mobile
di['pin'] = pin
for i,j in di.items():
    print(i,'=',j)


