x = 2























def demo():
    x = 3
    return x

def demo_global():
    global x
    return x

def square (x):
    x = x * x
    return x

def cube(x):
    return x * x * x

def double_square(x):
    pass #Returns None

def power(x,n):
    a = x
    while (n!=1):
        a = a * x
        n -= 1
    return a

def something(x):
    pass
    return cube(x)

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))



print(x)
print(demo())
print(demo_global())
print(square(x))
print(cube(x))
print(double_square(x))
print(power(x,3))
for a in range(5):
    print(square(a))
print(something(x))
print(factorial(5))