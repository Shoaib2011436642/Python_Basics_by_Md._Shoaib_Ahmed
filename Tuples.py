my_tuple = (1,2,3)

print(type(my_tuple))           #printing type (tuple type will be the result)

print(my_tuple)                 #printing the tuple

print(my_tuple[2])              #printing a specific value in the tuple

#Error
#my_tuple[2] = 5                #changing the tuple values and printing it will clause error
#print(my_tuple)

#Negetive Indexing - starts with -1 - Here -1 is the last value of the tuple or list
#Then reversely goes -2 , -3
print(my_tuple[-1])
print(my_tuple[-2])

#Range of indexes - printing multiple values with a specific range of indexes
my_tuple_2 = (1,2,3,4,5,6,7,8,9)
print(my_tuple_2[3:6])              #Here 3 is the starting index,
                                    #Here 6 indicates the index where values printed before it. Means 3 to 5.
                                    #Last index will not be included

