import math

type_of_figure = input()

if type_of_figure == "square":
    square_side = float(input())
    square_area= square_side * square_side
    print(f"{square_area:.3f}")
elif type_of_figure == "rectangle":
    width = float(input())
    lenght = float(input())
    rectangle_area = width * lenght
    print(f"{rectangle_area:.3f}")
elif type_of_figure == "circle":
    radius = float(input())
    circle_area = math.pi * radius * radius
    print(f"{circle_area:.3f}")
elif type_of_figure == "triangle":
    side = float(input())
    height = float(input())
    triangle_area = side * height / 2
    print(f"{triangle_area:.3f}")