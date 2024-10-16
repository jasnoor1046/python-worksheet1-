# roots of a qaudtratic eqution
import cmath

a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c= int(input("Enter the value of c: "))

# the quadratic equation is of the form ax^2 + bx +c = 0
# here discriminant will be calculated.

D= b^2 - 4*a*c 

# to calculate the roots
root1 = (-b-cmath.sqrt(D))/2*a
root2 = (-b+cmath.sqrt(D))/2*a

print("The roots of the given equation are: ", root1, "and", root2)