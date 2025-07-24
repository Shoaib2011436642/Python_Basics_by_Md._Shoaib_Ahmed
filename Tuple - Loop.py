my_tuple = ("messi", "ronaldo", "neymar", "yamal")

for i in my_tuple:
    print(i)                #prints all the tuple value using for loop

for x in range(len(my_tuple)):
    print(x)                        #prints all the indexes

for y in range(len(my_tuple)):
    print(my_tuple[y])              # prints all the values of indexes

for z in range(len(my_tuple)):
    print(f"Index = {z} , Value = {my_tuple[z]}")         #print Index and values together

#using while loop
i = 0                               #storing initial index value as 0
while i < len(my_tuple):            #loop will continue until index value is less than the tuple length
    print(my_tuple[i])              #prints the values
    i = i + 1                       #updates the index values, not doing so will cause infinite loop