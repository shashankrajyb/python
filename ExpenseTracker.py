import csv
def add_expense():
    date = input("Enter the date: ")
    category = input("Enter the Category: ")
    amount = int(input("Enter the amount: "))
    description = input("Enter th description: ")
f = open("ExpenseTracker.csv","w")
f.write(add_expense())