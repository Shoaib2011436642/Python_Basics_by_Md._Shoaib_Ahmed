a = 10          #Global scope
b = 20

def my_func():
    x = 5       #local scope

    global c    #defining a global scope in a user defined function
    c = 30

    print(x)
    print(a)    #we can access global scope in any user defined function

my_func()       #calling the function as we can't access the local scope within a function without calling it.
print(b)
print(c)