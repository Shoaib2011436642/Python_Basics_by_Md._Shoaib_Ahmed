li = ["afif", "messi", "rohit"]
li5 = [1, 3, 5 , 7]

#append
for i in li:                                    #adding values from other list in a different list variable. Goes sequentially.
    li5.append(i)                               #added values in li5 from li
print(li5)

#extend
li_ex = ["afif", "messi", "rohit"]
li5_ex = [1, 3, 5 , 7]

li_ex.extend(li5_ex)
print(li_ex)