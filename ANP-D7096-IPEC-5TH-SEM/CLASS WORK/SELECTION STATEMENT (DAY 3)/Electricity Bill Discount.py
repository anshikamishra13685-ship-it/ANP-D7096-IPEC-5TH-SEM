'''----------- Electricity Bill Discount---------------------------------- 
An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 
or more. Otherwise, no discount is applied. 
Write a Python program to accept the total bill amount from the user and display the final amount to 
be paid.
------------------------------------------------------------------ 
Sample Input 1 
Enter the electricity bill amount: 6200 
--------------------------------------------------------------------
Sample Output 1 
Discount Applied! 
Final Bill Amount: ₹5580.0 
----------------------------------------------------------------------
Sample Input 2 
Enter the electricity bill amount: 4200 
-------------------------------------------------------------------------
Sample Output 2 
No Discount Applied! 
Final Bill Amount: ₹4200 
 '''
#--------------------------------------------------------------------------
#take input from the user 
electricity_bill_amount = float(input("enter electricity bill amount(in rupees): "))
#check if the bill amount is greater than equal to 5000
if electricity_bill_amount>= 5000:
    discount = electricity_bill_amount * 0.10
    final_amount = electricity_bill_amount - discount
    print(f"final bill amount: rs{final_amount}")
    print("discount applied!")
else:
    final_amount = electricity_bill_amount 
    print(f"final bill amount: rs{final_amount}")
    print("no discount applied!") 


