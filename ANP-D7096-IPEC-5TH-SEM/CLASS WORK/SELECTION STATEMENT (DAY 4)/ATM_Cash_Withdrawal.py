''' ATM Cash Withdrawal  
Problem Statement 
A customer can withdraw money only if the requested amount does not exceed the available balance. 
Accept the account balance and withdrawal amount. 
• If withdrawal amount is less than or equal to balance, display: 
Transaction Successful 
• Otherwise display: 
Insufficient Balance 
Sample Input 
5000 
4500 
Sample Output 
Transaction Successful'''
#--------------------------------------------------------------------------------------
# Accept account balance from the user
balance = float(input())

# Accept withdrawal amount from the user
withdraw = float(input())

# Check if the withdrawal amount is within the available balance
if withdraw <= balance:
    # Display success message
    print("Transaction Successful")
else:
    # Display insufficient balance message
    print("Insufficient Balance")
    