import math
#x = 2

def hello(username):
    print("Hello,", username, "! All is fine!")
    print(x)

def f():
    print("Just this part is executed")

def square(x):
    return x * x

def cube(x):
    y = x * x * x
    return y

def power(x,n):
    a = x
    while (n!=1):
        a = a * x
        n -= 1
    return a
#print(square(x))
#print(cube(x))
#print(y)
print(power(2,6))


