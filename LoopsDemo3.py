#IF ELSE CONDITION
greeting ="Good morning"

if greeting == "Morning":
    print("Condition matches")
    print("second line")
else:
    print("Condition did not match")
print("if else code is completed")   #this line is independent of(not a part of) if else block.

#condition will not match as "Good morning" is not equal to "Morning"

a=4
if a>2:
    print("Condition matches")
    print("second line")
else:
    print("Condition did not match")
print("if else code is completed")


#FOR LOOP

obj=[2,3,5,7,9]         #list
for i in obj:
    print(i)

#print i * 2
for i in obj:
    print(i*2)      #will print multiple of 2

#print sum of first natural numbers i.e. 1+2+3+4+5=15
summ=0
for j in range(1, 6):        #will iterate from 1 to 6-1
    summ = summ + j
    print(summ)


#Example of for loop
print("*****************************************")
for k in range(1,10,2):
    print(k)


print("******************SKIPPING FIRST INDEX***********************")
for m in range(10):
    print(m)