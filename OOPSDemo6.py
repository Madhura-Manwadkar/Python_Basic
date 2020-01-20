#classes are user defined blueprint or prototype
#sum,multiplication,addition,constant
#methods,variables or class variables,instance variables, constructor etc

#self keyword is mandatoy for calling variable name into method
#instance and class variables have whole different purpose
#constructor name should be  __init__
#new keyword is not required when you create object


class Calculator:
    num = 100           #class variables

    #default constructor
    def __init__(self,a,b):
        self.firstNumber=a
        self.secondNumber=b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num    #or Calclator.num


obj = Calculator(2, 3)      #syntax to create object of a class in python
obj.getData()
print(obj.Summation())


obj = Calculator(4, 5)      #syntax to create object of a class in python
obj.getData()
print(obj.Summation())
