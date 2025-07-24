class father:
    car = "Honda Civic"         #defining properties of parent class
    phone = "S24 Ultra"
    notebook = "macbook"

class son(father):              #parent class inherited in the child class, to use the properties of parent class in child class
    a = ""                      #child class
    b = ""

x = son()                       #holding the child class in an object
print(x.car)                    #usage of parent class properties through child class
x.phone = "Iphone16"
print(x.phone)

y = father()                    #Even though the property value used in child from parent was modified,
print(y.phone)                  #The property value in parent will remain unchanged