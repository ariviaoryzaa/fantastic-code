import json 

# dictionary
identification = {
    "username" : "arivia",
    "password" : "test123test",
    "nickname" : "aryviass",
}

identification['age'] = 17
identification['game'] = 'valorant'

with open ('id.json', 'w') as file:
    id.json(identification, file, indent=4)
