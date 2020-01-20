values = [1,2,"rahul",4,5]
#List is a datatype that allows multiple values and can be with different datatypes.

print(values[0])     #1

print(values[3])  #4

print(values[-1])    #returns the last element

print(values[-2])    #returns the last second element

print(values[1:4])   #returns the element from 1 and 4 index

values.insert(3,"shetty")    #inserts shetty at 3rd index in list
print(values)

values.append("end")        #inserts end at end of list
print(values)

values[2] = "RAHUL"     #updating the value
print(values)

del values[0]           #deleted first element
print(values)



#TUPPLE
#tupple same as list datatype but immutable where updation is not possible
val = (1 ,2, "rahul" , 4, 5)

print(val[1])

#val[2]= "RAHUL"  #error because updation not possible so to update use list.
print(val[2])


#DICTIONARY

dic = {"a": 2, 4: "bcd", "c": "Hello world"}      #no rule such as double quotes for key or value ,
                                               # but double quotes should be used for string,
                                               #whether it is key or value.
print(dic[4])
print(dic["c"])         #put string in double quotes

dic[4]="rahul"          #updating the value, note: Keys must me immutable(unchanged)
print(dic[4])

#

dict = {}       #empty dictionary

dict["firstname"]="Rahul"   #adding key value pair to empty dictionary(dict)
dict["lastname"]="shetty"

print(dict)

dict["gender"]="Male"
print(dict)

print(dict["lastname"])












