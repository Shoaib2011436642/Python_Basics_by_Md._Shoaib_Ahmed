my_list = [1,6,7,15,105,99,240]                     #creating a list in array. List is an object.
                                                    #Number value in range 0-255. Or else will give error if we are converting to byte type.
print(my_list)                                      #prints the list

#bytes
x = bytes(my_list)                                  #converting the list (obj) in byte. Also storing it in a variable
print(x)                                            #byte value printing
print(type(x))                                      #get type format (byte)

#bytesarray
my_list2 = [2,3,8,17,45,220,105]
y = bytearray(my_list2)
print(type(y))

y[1] = 4                                            #Changing value in bytearray as mutable on index 1.
                                                    #index starts from 0.
                                                    #changing value in bytes will cause error as immuatble.
print(y[1])                                         #print the changes value
print(y)                                            #print the byte values of the list to see if the change worked for bytearray


