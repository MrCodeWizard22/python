# learning about different types of input in python 
#         @      @
             
#            ^

value=int (input("enter the value "))
value =value*5
print (value)
new=float(input("enter the value in float"))

print (new)
name =input("enter your name ")

print ("hello",name)
print(type(value))
print (type(name))
print (type(new))

x=10
print (type(x))
y=12.5
print (type(y))
z=x+y
print (z,type(z))

s='10010'
c=int (s,2)
print (c)
a='0xffd'
b=int (a,16)
print (b)
t='101010'
u=float(t)
print (u)

# ord->converting a character to string 
# unicode is a stirng of the code point which are num from zero


newstring='4'
conv=ord(newstring)
print("after converting the character to string ",conv)

num=400
newnum=oct(num)
print (newnum)

