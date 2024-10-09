def addtion(x,y):
    return("Addtion",x+y)
def subract(x,y):
    return("Subract",x-y)
def multiply(x=1,y=1):
    return("Multiply",x*y)
def division(x,y):
    return("Division",x/y)
def myfunc():
    pass

def peoples(*names):
    return print("Students in My Class",names)

def myfunc1(x,y,z,/,*,a):
    print(x+y+z+a)
    
myfunc1(1,2,3,4,a=100)