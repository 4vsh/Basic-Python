#calculating area

import math

def calculate_rectangle_area():
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    area = length * width
    print(f"The total area of the rectangle is {area} cm²")

def calculate_circle_area():
    radius = float(input("Enter Radius: "))
    area = math.pi * radius ** 2
    print(f"The total area of the circle is {area} cm²")

def calculate_triangle_area():
    base = float(input("Enter Base: "))
    height = float(input("Enter Height: "))
    area = 0.5 * base * height
    print(f"The total area of the triangle is {area} cm²")

def main():
    print("Choose the shape to calculate the area:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        calculate_rectangle_area()
    elif choice == 2:
        calculate_circle_area()
    elif choice == 3:
        calculate_triangle_area()
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

