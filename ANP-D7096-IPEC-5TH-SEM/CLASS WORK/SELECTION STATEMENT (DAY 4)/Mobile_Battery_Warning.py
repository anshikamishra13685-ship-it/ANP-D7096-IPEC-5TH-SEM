'''Mobile Battery Warning 
Problem Statement 
A smartphone displays a low battery warning only when the battery percentage falls below 15%. 
Write a Python program to accept the battery percentage. 
If the battery is below 15, display: 
Connect Charger Immediately 
Otherwise, display nothing. 
Sample Input 
10 
Sample Output 
Connect Charger Immediately '''
#-----------------------------------------------------------------------------------------
# Accept battery percentage from the user
battery = int(input())

# Check if battery percentage is below 15
if battery < 15:
    # Display warning message
    print("Connect Charger Immediately")