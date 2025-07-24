class mymethod:
    def instance_method(self):
        print("This is instance method")

    @classmethod
    def class_method(cls):
        print("This is class method")

    @staticmethod
    def static_method():        #no arguments needs to be passed
        print("This is static method")

x = mymethod()  #object declaration for instance method
x.instance_method()     #can't call it directly from class, will cause error

x.class_method()    #or     #can directly call from class
mymethod.class_method()

x.static_method()   #or     #same as class method
mymethod.static_method()