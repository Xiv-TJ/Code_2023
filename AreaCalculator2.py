print("Welcome to the Secondary 2 Volume Calculator.")
print("Before we continue, please state the area of the solid you would like to find.")
math = input("You can choose either; A: Cone, B: Pyramid or C: Sphere?: ")
if math == "A":
    length = float(input("What is the height of the cone, in cntimetres?: "))
    width = float(input("What is the width of the cone, in centimetres?: "))
    cone = (1/3 * 3.14 * length * width**2)
    print("The area of the cone is " + str(cone) + "cm!")
elif math == "B":
    length = float(input("What is the height of the pyramid, in centimetres??: "))
    width = float(input("What is the base of the pyramid, in centimetres?: "))
    pyramid = (1/3 * length * width)
    print("The area of the pyramid is " + str(pyramid) + "cm!")
elif math == "C":
    radius = float(input("What is the radius of the sphere, in centimetres?: "))
    sphere = (4/3 * 3.14 * radius**2)
    print("The area of the sphere is " + str(sphere) + "cm!")
else:
    print("Please leave.")
print("Thank you for using the Secondary 2 Calculator!")