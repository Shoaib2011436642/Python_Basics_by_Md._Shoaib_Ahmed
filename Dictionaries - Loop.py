my_dict = {
    "brand": "Toyota",
    "Color": "White",
    "Price": 35000
}

#getting key names
for x in my_dict:
    print(x)

for y in my_dict.keys():        #using keys function
    print(y)

#getting values
for a in my_dict:
    print(my_dict[a])

for b in my_dict.values():      #using values function
    print(b)

#geting key and value both, using items function
for c, d in my_dict.items():
    print(c,d)