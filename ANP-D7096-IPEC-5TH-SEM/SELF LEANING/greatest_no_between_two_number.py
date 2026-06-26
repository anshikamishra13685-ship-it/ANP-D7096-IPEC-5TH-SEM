'''greatest_no_between_two_number
a user want to find out gratest number between two number'''
#---------------------------------------------------------------------
# Program to find the greatest number between two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is the greatest number.")
elif b > a:
    print(b, "is the greatest number.")
else:
    print("Both numbers are equal.")
     