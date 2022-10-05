#8223190 – Shelemiah Sotelo
#Task 2
#Geometry Calculator – Using function

print("Geometry Calculator\n 1. Calculate the Area of a Circle\n 2. Calculate the Area of a Rectangle\n 3. Calculate the Area of a Triangle\n 4. Quit\n Enter your choice (1-4): ")
choice = input().strip()
choice = int(choice)

if choice == 1:
    print("Enter radius:")
    rad = input()
    rad = float(rad)

    circleArea = 3.14 * (rad * rad)
    print("The area of the circle is " + str(circleArea) + "sq. cm.")
    
elif choice == 2:
    print("Enter width:")
    width = input()
    width = float(width)

    print("Enter length:")
    length = input()
    length = float(length)
    rectangleArea = (width * length)
    print("The area of the rectangle is " + str(rectangleArea) + "sq. cm.")
 
elif choice == 3:
    print("Enter base:")
    base = input()
    base = float(base)

    print("Enter height:")
    height = input()
    height = float(height)
    triangleArea = .5 * (base * height)
    print("The area of the triangle is " + str(triangleArea) + "sq. cm.")
    
else:
    print("Thank you!")    
