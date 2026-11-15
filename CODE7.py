#WAPP to add digit of a given decimal number 
number = int(input("Enter a decimal number: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10
print("Sum of digits is:", sum_of_digits)