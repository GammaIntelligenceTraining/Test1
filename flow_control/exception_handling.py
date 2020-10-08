# Exception handling sample
a, b = input("Two integer number:").split(",")
try:
 if (int(a) % int(b)==0):
    print(int(a), " could be divided by ",int(b)," without remainder")
 else:
     print(int(a), " could not be divided by ",int(b)," without remainder")
except ZeroDivisionError:
    print("Could not divided by zero")
except ValueError:
    print("Please use only numbers. Verify that you are using 2 numbers")
