from triangle import Triangle
def main():
    # Create triangles with different constructors
    triangle1 = Triangle()
    print(f"Triangle1 created with default sides: {triangle1}")
    print(f"Triangle1 perimeter: {triangle1.perimeter()}")
    print(f"Triangle1 is right-angled: {triangle1.is_right_angled()}")

    triangle2 = Triangle(3)
    print(f"Triangle2 created with one side: {triangle2}")
    print(f"Triangle2 perimeter: {triangle2.perimeter()}")
    print(f"Triangle2 is right-angled: {triangle2.is_right_angled()}")

    triangle3 = Triangle(3, 4)
    print(f"Triangle3 created with two sides: {triangle3}")
    print(f"Triangle3 perimeter: {triangle3.perimeter()}")
    print(f"Triangle3 is right-angled: {triangle3.is_right_angled()}")
    
    triangle4 = Triangle(3, 4, 5)
    print(f"Triangle4 created with three sides: {triangle4}")
    print(f"Triangle4 perimeter: {triangle4.perimeter()}")
    print(f"Triangle4 is right-angled: {triangle4.is_right_angled()}")    
    
    # copy triangle
    triangle_copy = Triangle(triangle4)
    print(f"Copied Triangle: {triangle_copy}")
    print(f"Copied Triangle perimeter: {triangle_copy.perimeter()}")
    print(f"Copied Triangle is right-angled: {triangle_copy.is_right_angled()}")
    
    # Check object count
    print(f"Total Triangle objects created: {Triangle.object_count()}")

if __name__ == "__main__":
     main()
        