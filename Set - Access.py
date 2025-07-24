my_set = {1,2,3,4,"4",5, "Messi"}

#Using for loop
for i in my_set:
    print(i)

#Access a specific value if it is present in the set or not
print("Messi" in my_set)        #Hard coding the specific value followed by the "in" function calling the set variable
                                #If the value is present, output will show "True", if not then "False"