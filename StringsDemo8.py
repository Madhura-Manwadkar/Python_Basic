#Strings

str = "MadhuraManwadkarAcademy.com"
str1 = "Consulting firm"
str2 = "MadhuraManwadkar"
str3 = "shdbfjhjfv"
print(str[1])       #will print a

print((str[0:7]))      #will print Madhura (to get substring)

print(str+str1)           #concatenation

#check whether one string is present in another string

print(str2 in str)      #returns true

print(str3 in str)      #returnd false

#split string

var = str.split(".")           #will split from '.'
print(var)
print(var[0])       #prints Madhura ManwadkarAcademy
print(var[1])       #prints com

#rempves white spaces using Strip function

str4 = "    great    "
print(str4.strip())


#remove left and right white spaces

print(str4.lstrip())        #removes left spaces
print(str4.rstrip())        #removes right spaces


