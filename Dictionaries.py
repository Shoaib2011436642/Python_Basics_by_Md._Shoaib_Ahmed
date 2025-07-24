my_dict = {                             #Simple dictionary variable, storing with keys:Values
    "brand": "Tesla",
    "Color": "White",
    "Price": 35000
}

print(my_dict)                          #Output: Whole info in the dict variable
print(my_dict["brand"])                 #Getting a specific key value using 3rd bracket

my_dict_2 = {
    "Player1": {
        "name": "Messi",
        "club": "Miami",
        "country": "Argentina"
    },
    "Player2": {
            "name": "Ronaldo",
            "club": "Nasser",
            "country": "Portugal"
    },
    "Player3": {
                "name": "Neymar",
                "club": "Santos",
                "country": "Brazil"
    }
}

print(my_dict_2)
print(my_dict_2["Player1"])
print(my_dict_2["Player3"]["club"])         #Getting a specific key value of a specific player
                                            #1st [] indicates the specific key(player),
                                            # 2nd [] indicates another specific key(Country of the player)
