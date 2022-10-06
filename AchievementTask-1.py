#8223190 – Shelemiah Sotelo
#Task 1
#Geometry Calculator


print("Geometry Calculator\n 1. Calculate the Area of a Circle\n 2. Calculate the Area of a Rectangle\n 3. Calculate the Area of a Triangle\n 4. Quit\n Enter your choice (1-4): ")
choice = input()
choice = int(choice)

if choice == 1:
    print("Enter radius:")
    rad = input()
    rad = float(rad)

    circleArea = 3.14 * (rad * rad)
    circlePer = 2* 3.14 * (rad)
    print("The area of the circle is " + str(circleArea) + "sq. cm.")
    print("The perimeter of the circle is " + str(circlePer) + "cm.")
    
elif choice == 2:
    print("Enter width:")
    width = input()
    width = float(width)

    print("Enter length:")
    length = input()
    length = float(length)
    rectangleArea = (width * length)
    rectanglePer = (width * length)
    print("The area of the rectangle is " + str(rectangleArea) + "sq. cm.")
    print("The perimeter of the rectangle is " + str(rectanglePer) + "cm.")
    
 
elif choice == 3:
    print("Enter base:")
    base = input()
    base = float(base)
        
    print("Enter side1:")
    side1 = input()
    side1 = float(side1)
    
    print("Enter side2:")
    side2 = input()
    side2 = float(side2)

    print("Enter height:")
    height = input()
    height = float(height)
    triangleArea = .5 * (base * height)
    trianglePer = (side1 + side2 + base)
    print("The area of the triangle is " + str(triangleArea) + "sq. cm.")
    print("The perimeter of the triangle is " + str(trianglePer) + "cm.")
    
else:
    print("Thank you!")    

