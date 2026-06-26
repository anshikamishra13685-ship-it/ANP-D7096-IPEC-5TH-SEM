'''Loan Approval System 
Problem Statement 
A bank evaluates loan applications using: 
• Credit Score ≥ 750  
• Annual Income ≥ ₹8,00,000  
• Existing Loan Amount ≤ ₹2,00,000  
Conditions: 
• All conditions satisfied → Approved  
• Only one condition fails → Manual Review  
• More than one condition fails → Rejected  
Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 
Sample Output 
Loan Status: Manual Review 
Reason: Income criteria not satisfied.'''
#--------------------------------------------------------------------------
# Loan Approval System

credit_score = int(input("Enter Credit Score: "))
income = float(input("Enter Annual Income: "))
existing_loan = float(input("Enter Existing Loan Amount: "))

failed = 0
reason = ""

# Check Credit Score
if credit_score < 750:
    failed += 1
    reason = "Credit Score criteria not satisfied."

# Check Annual Income
if income < 800000:
    failed += 1
    reason = "Income criteria not satisfied."

# Check Existing Loan Amount
if existing_loan > 200000:
    failed += 1
    reason = "Existing Loan Amount criteria not satisfied."

# Decision
if failed == 0:
    print("Loan Status: Approved")
elif failed == 1:
    print("Loan Status: Manual Review")
    print("Reason:", reason)
else:
    print("Loan Status: Rejected") 
 
