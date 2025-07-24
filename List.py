li = ["afif", "messi", "rohit"]                 #storing values in list variable
li2 = [1,2,3]
li3 = [True, False, True]
li5 = [1, 3, 5 , 7]
li4 = []

print(li3)                                      #printing list values
print(type(li3))                                #printing list type

#change value in list
li[2] = "Shakib"                                #changing a value in index 2 of li
print(li)
print(li[2])                                    #printing the changed index value

for i in li:                                    #printing value in new line but in sequence - using loop
    print(i)

#add item in list
li6 = [22, 55, 66]
li6.append(111)                                 #append - add value in the list
print(li6)

li6.insert(1, 44)               #inserting value in index 1
print(li6)                                      #here index 1 new value added. previous value shifted to next index.

for i in li:                                    #storing li values in li4
    li4.append(i)
print(li4)

for i in li:                                    #adding values from other list in a different list variable. Goes sequentially.
    li5.append(i)
print(li5)

#copy a list in other list variable
li_1c = [1, 2, 3, 'banana', True]
li_2c = li_1c.copy()
print(li_2c)