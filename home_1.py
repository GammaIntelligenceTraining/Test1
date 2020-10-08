import random

def list_generator(x):
    while x > 0:
        list.append(random.randrange(int(nmin), int(nmax) + 1))
        x = x - 1
    return list

def pick_minimumvalues():
    counter = 3
    while counter > 0:
        min_list.append(min(list))
        list.remove(min(list))
        counter = counter - 1
    return min_list

while True:
    try:
        n, nmin, nmax = input("Please enter list length, minimal list element and maximum list element. Use space as separator, must be whole numbers: ").split(" ")
        n = int(n)
        nmin = int(nmin)
        nmax = int(nmax)
        break
    except ValueError:
        print("Number should be an integer")
    #print("You entered incorrect values!")

list = []
min_list = []

print(list_generator(n))
print(pick_minimumvalues())