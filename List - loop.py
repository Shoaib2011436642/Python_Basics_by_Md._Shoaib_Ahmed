#for loop
loop_list = [55, 66, "banana", True]
for i in loop_list:
    print(i)

#using range & len to get index numbers sequentially or iterablly
loop_list_1 = [55, 66, "banana", True]
for i in range(len(loop_list_1)):                   #don't forget the colon (:)
    print(i)

#while loop
loop_list_2 = [55, 66, "banana", True]
i = 0                                              #index number starts from 0, so count variable i value stores as 0
while i < len(loop_list_2):                        #The loop will run until the index number is less than i
    print(loop_list_2[i])                          #printing values one by one through index number
    i = i + 1                                      #updating the index count

#list comprehension
loop_list_3 = [55, 66, "banana", True]             #adding list values of another list variable
loop_list_4 = [44, 77, "mango", False]

for i in loop_list_3:
    loop_list_4.append(i)
print(loop_list_4)                                #added list values index number starts after previous final index number

#updating the values into double (*2)
loop_list_d = [1,2,3,4,5]
for i in loop_list_d:
    print(i * 2)

#double in one line'
loop_list_d1 = [1,2,3,4,5]
double = [i*2 for i in loop_list_d1]
print(double)