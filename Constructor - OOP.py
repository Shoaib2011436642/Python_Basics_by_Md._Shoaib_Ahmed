class sports:   #creating constructor class

    def __init__(self, name, country):  #init: built-in constructor method, runs when a new object is made
                                        #self: default parameter - makes the data stick to the object
        print(f"He is {name}.He plays for {country}.")

x = sports("Messi", "Argentina")
