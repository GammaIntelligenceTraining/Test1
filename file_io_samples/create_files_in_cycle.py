for x in range(5):
    filename='name'+str(x)+'.txt'
    f = open(filename,"w")
    f.write(filename)
    f.close()




