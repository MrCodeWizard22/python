# learning conditionnal statements if and else in python 
# problem :- age as input and test whether he can drive a car or not 18+ can drive the car if he has the car 
age =int (input("enter your age "))
car=(input("does he own a car"))
if(age>=18):
    if(car=="YES"):
        print("you can drive the car")
    else:
        print("first own a car ")
else:
    if(car=="YES"):
        print ("you are under age")
    else: 
        print ("you can't drive ,also you don't have car")

