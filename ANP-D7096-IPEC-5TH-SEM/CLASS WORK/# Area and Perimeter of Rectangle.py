# Area and Perimeter of Rectangle

length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

if length > 0 and breadth > 0:
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area of Rectangle =", area)
    print("Perimeter of Rectangle =", perimeter)