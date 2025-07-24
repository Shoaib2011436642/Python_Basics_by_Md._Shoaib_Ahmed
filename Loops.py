#while loop
count = 0                       #count initial value set to 0
while count < 5:                    #count < 5, this condition means it will run the loop till the condition becomes false (Here 5 times)
    print("count is ", count)
    #count = count + 1      #or
    count += 1                      #increamenting count value, not using it will cause infinite loop.

#for loop
fruits = ["apple", "banana", "cherry"]      #creating a sequence (list) to use for loop
for i in fruits:
    print(i)