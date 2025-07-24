#Break
for i in range(9):                  #range 0 to 8, Here 9 indicates the values before it
    if i == 4:
        break                       #the break function executes the conditional statement and halts the loop to continue.
    print(i)

#break using a list
my_list = ["apple", "banana", "cherry", "mango", "orange", "kiwi", "melon"]
for j in range(len(my_list)):
    if j == 3:
        break
    print(j)
    print(my_list[j])

#continue
for k in range(9):
    if k == 4:
        continue            #the continue function halts the conditional statement and let the loop continue
    print(k)