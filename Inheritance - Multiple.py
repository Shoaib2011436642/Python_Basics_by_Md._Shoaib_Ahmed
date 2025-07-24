class father:
    car = "Honda Civic"
class father2:
    phone = "S24 Ultra"
class father3:
    Laptop = "Macbook Pro"

class son(father, father2, father3):  #inheriting multiple parent class
    a = ""
    b = ""

x = son()
print(x.car)        #usage of different properties of different parent class through child class
print(x.phone)
print(x.Laptop)