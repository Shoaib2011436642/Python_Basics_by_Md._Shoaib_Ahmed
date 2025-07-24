#remove function
my_set1 = {1,2,3,4}
my_set1.remove(3)           #removes a specific value
print(my_set1)


#discard function
my_set2 = {1,2,3,4}
my_set2.discard(6)         #Here value "6" is not present, but printing it will not cause any error like remove function
print(my_set2)             #Though it works exactly same as remove function.


#pop method
my_set3 = {1,2,3,4}
my_set3.pop()              #can pop any of the value. here popped the first one as sets are unordered.
print(my_set3)

#clear
my_set4 = {1,2,3,4}
my_set4.clear()            #removes all the values. Makes it an empty set.
print(my_set4)