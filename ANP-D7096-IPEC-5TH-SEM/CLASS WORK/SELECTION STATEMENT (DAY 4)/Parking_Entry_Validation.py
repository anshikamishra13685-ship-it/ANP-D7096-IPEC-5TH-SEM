'''Parking Entry Validation  
Problem Statement 
Only vehicles having a valid parking pass are allowed to enter a private parking area. 
Accept either 1 (Valid Pass) or 0 (No Pass). 
• If the input is 1, display: 
Entry Allowed 
• Otherwise display: 
Entry Denied 
Sample Input 
0 
Sample Output 
Entry Denied '''
#------------------------------------------------------------------------------------
# Accept parking pass status from the user
parking_pass = int(input())

# Check if the parking pass is valid
if parking_pass == 1:
    # Display entry allowed message
    print("Entry Allowed")
else:
    # Display entry denied message
    print("Entry Denied")