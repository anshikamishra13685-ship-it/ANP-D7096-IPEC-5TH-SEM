''' Courier Delivery Charge 
Problem Statement 
A courier company calculates delivery charges based on the package weight. 
• Weight up to 2 kg → ₹50  
• Weight greater than 2 kg and up to 5 kg → ₹100  
• Weight greater than 5 kg → ₹180  
Write a Python program to display the delivery charge. 
Sample Input 
4 
Sample Output 
Delivery Charge = ₹100'''
#------------------------------------------------------------------------------
weight = float(input())

if weight <= 2:
    print("Delivery Charge = ₹50")
elif weight <= 5:
    print("Delivery Charge = ₹100")
else:
    print("Delivery Charge = ₹180") 
 
