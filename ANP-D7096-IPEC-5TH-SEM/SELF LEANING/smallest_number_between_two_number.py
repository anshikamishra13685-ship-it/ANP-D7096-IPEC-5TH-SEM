'''Find the Smallest Number Between Two Numbers'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print(a, "is smaller")
elif b < a:
    print(b, "is smaller")
else:
    print("Both numbers are equal")