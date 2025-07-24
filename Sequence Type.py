#list type
x = [1,2,3,'afif',5,'nsu']          #list type - changeable or mutable
print(x)
print(x[2])
print(type(x))

x[1] = 2011
print(x[1])                         #updated the 2 no index
print(x)

#tuple type
y = (1,2,3,4)                       #tuple type immutable - can't update
print(y)
print(type(y))

#range type
z = range(7)
print(z)

for i in z:
    print(i)