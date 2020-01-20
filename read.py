file = open("test.txt")
#Read all the contents of file
#read n number of characters by passing paameter
#print(file.read(5))

#read  one single line at a time readline()

#print(file.readline())    #reads linewise
#print(file.readline())
#print(file.readline())



#print line by line using readline method.

#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()

#values = {abc, bvdsf. "cat", dog, elephant}

for line in file.readlines():           #reads every index (like from list) (every line in file)
    print(line)




file.close()