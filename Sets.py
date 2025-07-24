my_set = {1,2,3,4,4,5,5}            #Same values here are multiple times, but a set will only contain a specific value a single time.

print(my_set)                       #multiple values are shown here single time.

my_set2 = {1, True, False, "Messi", 3}      #In set True values are not shown, But it shows the false value.
print(my_set2)                              #Sets are unordered.
                                            #So it showed a different order of values. Not like the order that was coded as input.

print(type(my_set))

my_set3 = {1,2,3,4,"4",5}                 #Same number but different data type
print(my_set3)                              #Here 4 was shown multiple times as both values had different data types.
                                            #One was string, One was Integer.

print(len(my_set3))                         #Len shows the number of items present in the set