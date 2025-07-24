my_dict = {
    "brand": "Toyota",
    "Color": "White",
    "Price": 35000
}

#Add item
my_dict["model"] = "Crown"
print(my_dict)

#pop method
my_dict.pop("Color")        #pops a specific key
print(my_dict)

#popitem method
my_dict.popitem()           #pops the final key
print(my_dict)