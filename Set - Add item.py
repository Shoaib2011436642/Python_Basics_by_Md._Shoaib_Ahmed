#adding a new item into a set
my_set = {1,2,3,4}
my_set.add(5)                   #using set function

print(my_set)


#merging 2 sets or updating or copying values from another set to my desired set
set1 = {"Messi", "Ronaldo", "Neymar"}
set2 = {"Mbappe", "Haaland", "Yamal"}

set1.update(set2)                   #using update function alongside the desired set variable to be updated from a set.
print(set1)

#Can also update from a list or tuple into a set
set3 = {1,2}
tuple1 = (3,4)
list1 = [5,6]

set3.update(tuple1)
set3.update(list1)

print(set3)
