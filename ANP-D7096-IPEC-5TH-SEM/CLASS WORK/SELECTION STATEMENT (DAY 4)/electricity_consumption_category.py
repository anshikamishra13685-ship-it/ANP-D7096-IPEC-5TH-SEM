'''Electricity Consumption Category (if...elif...else Statement) 
Problem Statement 
An electricity department categorizes households based on monthly electricity consumption. 
• Up to 100 units → Low Consumption  
• 101-300 units → Moderate Consumption  
• Above 300 units → High Consumption  
Write a Python program to display the consumption category. 
Sample Input 
245 
Sample Output 
Moderate Consumption'''
#--------------------------------------------------------------------------------------
# Accept monthly electricity consumption from the user
units = int(input())

# Check the consumption category
if units <= 100:
    # Low consumption
    print("Low Consumption")
elif units <= 300:
    # Moderate consumption
    print("Moderate Consumption")
else:
    # High consumption
    print("High Consumption")