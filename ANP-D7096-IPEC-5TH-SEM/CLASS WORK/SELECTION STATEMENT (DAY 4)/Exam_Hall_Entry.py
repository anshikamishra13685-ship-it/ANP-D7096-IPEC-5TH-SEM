'''Exam Hall Entry 
Problem Statement 
Students are allowed to enter the examination hall only if they are carrying their admit card. 
Accept input as: 
• 1 → Admit Card Available  
• 0 → Admit Card Not Available  
If the input is 1, display: 
Enter Examination Hall 
Otherwise, do not display anything. 
Sample Input 
1 
Sample Output 
Enter Examination Hall'''
#----------------------------------------------------------------------------------------
# Accept admit card status from the user
admit_card = int(input())

# Check if the student has an admit card
if admit_card == 1:
    # Display entry message
    print("Enter Examination Hall")
    