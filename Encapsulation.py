class account:   #constructor class
    def __init__(self, name, password):
        self.name = name            #instance variable - Public (accessible from outside)
        self.__password = password      #used encapsulation (__)before the parameter variable - keeps it private or hidden

p1 = account(name="Ezio Auditore", password="abc11225")
print(p1.name)
#print(p1.password)     #running it will cause error, as the passed parameter variable was private or encapsulated