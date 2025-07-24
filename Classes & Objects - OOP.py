class my_class:
    name = ""
    country = ""

x = my_class()              #holding the class in a variable called object
y = my_class()
x.name = "Messi"            #updating the values in the class property(name). Here, obj(x).property
y.name = "Neymar"
print(x.name)               #print that property
print(y.name)