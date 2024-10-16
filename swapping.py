# swapping without using third variable
a= int(input("Enter the first value"))
b= int(input("Enter the second value"))

a,b = b,a

print("value of a and b after swapping are:",a, "and b:",b)
