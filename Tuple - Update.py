my_tuple = (1,2,3,4,5)

#Converting to List
con_list = list(my_tuple)           #List conversion
con_list.append(6)                  #adding value by append - will add it in final index
print(con_list)

my_tuple = tuple(con_list)          #Changing it back to tuple after updating
