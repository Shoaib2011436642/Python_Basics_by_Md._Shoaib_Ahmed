#union method
my_set1 = {1,2,3,4}
my_set2 = {5,6}

my_set3 = my_set1.union(my_set2)            #Same as update method. But we can also do union method for a different set variable.
print(my_set3)

#update method
my_set4 = {1,2,3,4}
my_set5 = {5,6}

my_set4.update(my_set5)
print(my_set4)