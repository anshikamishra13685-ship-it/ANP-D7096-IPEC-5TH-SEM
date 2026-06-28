'''Restaurant Bill Discount 
Problem Statement 
A restaurant offers discounts based on the total bill amount. 
• Bill below ₹1000 → No Discount  
• ₹1000–₹2999 → 10% Discount  
• ₹3000 or more → 20% Discount  
Write a Python program to determine the applicable discount. 
Sample Input 
3200 
Sample Output 
20% Discount Applied'''
#------------------------------------------------------------------------------------------
# Accept the total bill amount from the user
bill = float(input())

# Check the bill amount and apply the appropriate discount
if bill < 1000:
    # No discount
    print("No Discount")
elif bill < 3000:
    # 10% discount
    print("10% Discount Applied")
else:
    # 20% discount
    print("20% Discount Applied")
    