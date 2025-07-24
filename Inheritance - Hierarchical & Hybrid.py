#Hierarchical
class Father:
    car = "Toyota Corolla"

class Son1(Father):
    phone = "iPhone 15"

class Son2(Father):
    laptop = "Dell XPS"
x = Son1()
y = Son2()
print(x.car)
print(y.laptop)

#Hybrid
class GrandFather:
    house = "2-Storey Building"
class Father(GrandFather):
    car = "Tesla Model Y"
class Uncle(GrandFather):
    business = "Textile Shop"
class Son(Father, Uncle):
    phone = "Pixel 9"
x = Son()
print(x.house)
print(x.car)
print(x.business)
print(x.phone)