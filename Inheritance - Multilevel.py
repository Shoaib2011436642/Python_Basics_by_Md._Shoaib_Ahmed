class father:
    car = "Honda Civic"
class son1(father):             #inheriting father in son1
    phone = "S24 Ultra"
class son2(son1):               #inheriting son1 in son2. Here father is also inherited in son2 through son1
    Laptop = "Macbook Pro"

class son3(son2):  #father, son1, son2 inherited in son3 through son2
    a = ""

x = son3()
print(x.car)
print(x.phone)
print(x.Laptop)