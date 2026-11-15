#WAPP to print a table for a given number 
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)