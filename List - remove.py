#remove function
li = [1 ,2, 3, "banana", False]                 #For remove - put the exact value in the parenthesis
li.remove(2)
li.remove("banana")
print(li)

#pop function
li_1 = [1 ,2, 3, "banana", False]              #pop - removes a certain index value
li_1.pop(3)
li_1.pop()                                     #no index value - removes the final index value
print(li_1)

#del function
li_2 = [1 ,2, 3, "banana", False]
del li_2[0]                                    #same as pop - here we use third bracket [] for index number
print(li_2)
del li_2                                       #deleted the entire list with the variable. printing it will cause error.

#clear function
li_3 = [1 ,2, 3, "banana", False]
li_3.clear()                                   #Makes the list empty - no values
print(li_3)
