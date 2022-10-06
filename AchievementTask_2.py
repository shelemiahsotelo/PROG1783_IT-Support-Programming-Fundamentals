#8823190 - Shelemiah Sotelo
#Task2 
#Geometry Calculator – Using function

print("Geometry Calculator\n 1. Calculate the Area of a Circle\n 2. Calculate the Area of a Rectangle\n 3. Calculate the Area of a Triangle\n 4. Quit\n Enter your choice (1-4): ")
choice = input().strip()
choice = int(choice)

if choice == 1:
    print("Enter radius:")
    rad = input()
    rad = float(rad)

    def circleArea(rad):
        area = 3.14 * (rad * rad)
        return area

    print("The area of the circle is", circleArea(rad), " sq. cm.")

    def circlePer(rad):
        per = 3.14 * (2 * rad)
        return per

    print("The perimeter of the circle is", circlePer(rad), " cm.")
    
elif choice == 2:
    print("Enter width:")
    width = input()
    width = float(width)

    print("Enter length:")
    length = input()
    length = float(length)
    
    def rectangleArea(length, width):
        area = (length * width)
        return area

    print("The area of the rectangle is", rectangleArea(length, width), " sq. cm.")

    def rectanglePer(length, width):
        per = (2 * length) + (2 * width)
        return per

    print("The perimeter of the rectangle is", rectanglePer(length, width), " cm.")
    
 
elif choice == 3:
    print("Enter base:")
    base = input()
    base = float(base)

    print("Enter height:")
    height = input()
    height = float(height)
    
    print("Enter side1:")
    side1 = input()
    side1 = float(side1)
    
    print("Enter side2:")
    side2 = input()
    side2 = float(side2)
    
    def triangleArea(base, height):
        area = .5 * (base * height)
        return area

    print("The area of the triangle is", triangleArea(base, height), " sq. cm.")

    def trianglePer(base, side1, side2):
        per = (side1 + side2 + base)
        return per

    print("The perimeter of the triangle is", trianglePer(base, side1, side2), " cm.")    
    
    
else:
    print("Thank you!")    