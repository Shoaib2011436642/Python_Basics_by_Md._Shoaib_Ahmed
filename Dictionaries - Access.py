my_dict = {
    "Player1": {"name": "Messi","club": "Miami","country": "Argentina"},
    "Player2": {"name": "Ronaldo","club": "Nasser","country": "Portugal"},
    "Player3": {"name": "Neymar","club": "Santos","country": "Brazil"}
}

#Get method
x = my_dict.get("Player1")
print(x)

#Getting all Key names using keys function
y = my_dict.keys()
print(y)

#Both Get & Keys method provides us only the information of parent keys, not for nested

#Getting all the values using values function
z = my_dict.values()
print(z)