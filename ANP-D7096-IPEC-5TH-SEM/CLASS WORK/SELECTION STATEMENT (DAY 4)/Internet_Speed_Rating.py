'''Internet Speed Rating  
Problem Statement 
An Internet Service Provider categorizes connection quality based on download speed. 
• Less than 25 Mbps → Slow  
• 25-99 Mbps → Good  
• 100 Mbps or above → Excellent  
Write a Python program to display the connection quality. 
Sample Input 
120 
Sample Output 
Excellent Connection'''
#-------------------------------------------------------------------------------------
# Accept internet download speed from the user
speed = float(input())

# Check the internet speed and display the connection quality
if speed < 25:
    # Slow connection
    print("Slow Connection")
elif speed < 100:
    # Good connection
    print("Good Connection")
else:
    # Excellent connection
    print("Excellent Connection")