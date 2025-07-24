class sports:   #constructor class
    def __init__(self, name, club, country):
        self.name = name            #instance variable - Public (accessible from outside)
        self.club = club
        self.country = country
class football(sports):     # executed classes through constructor class
    pass
class cricket(sports):
    pass
p1 = football("Messi","Miami","Argentina")
print(p1.name, p1.club, p1.country)
c1 = cricket("Kohli", "Bengaluru", "India")
print(c1.name, c1.club, c1.country)