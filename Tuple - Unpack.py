my_tuple = ("messi", "ronaldo", "neymar", "yamal")

(a,b,c,d) = my_tuple            #storing each values of the tuple in each variable
                                #Will cause error if we don't store all the values separately
print(a)                        #printing the stored separated values
print(d)

#Storing all values in a single variable using Asterisk (*)
(*d,) = my_tuple            # * first, then variable, then lastly don't forget to use coma(,)
print(d)

(*e, f, g) = my_tuple       #here e variable will store all the values before each separated f & g variable
print(e)                    # e variable will print values before the separated values of f & g variable
print(g)

(h,i,*j,) = my_tuple        #here after each separated values in h & i variable, j variable will store the rest
print(j)