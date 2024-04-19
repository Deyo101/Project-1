
l = int(input("Input the length: "))
b = int(input("Input the breadth: "))
h = int(input("Input the height: "))

def v_cuboid(a, b, c):
    length = a
    breadth = b
    height = c
    volume = length *breadth * height
    return f"The volume of this cuboid is {volume}"
print (v_cuboid(l,b,h))

#remove the l, b, h from the function and make it a global variable
#and write in a way that you can pass any input into the functions
#use the return statement
