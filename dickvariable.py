# a variable acts as a container that stores data values
#declaring variables
x = 5 #x is the variable
y = 10 # y is another variable
print(x + y) #displays the sum off variable x and variable y
# output will be 15

# storing string data type in variables
t = "john "
z = "peters"
print(t + z)
# output will be john peters
y,x= (10,15)
print(x,y)
print ("the sum of x and y is ",x + y)
# A floating point
salary=1456.8
# An integer
age=45
#
a=b=c =10
print(a)
print(b)
print(c)
a,b,c = 1,50.5,"python programming"
print(a)
print(b)
print(c)

def f():
    global s
    print (s)
    s = "programming in python"

f()
s = "python is great"
print(s)