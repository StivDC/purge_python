cardiff_uni = {

    "name": "Cardiff University",

    "description": "",

    "exits": {"east": "Blackweir Tavern", "west": "Bute Park", "south": "Library"}
    
}

blackweir_tavern = {
     "name": "Blackweir Tavern",

    "description": "",

    "exits": {"east": "Lidl", "west": "Cardiff University"}
}

bute_park = {
     "name": "Bute Park",

    "description": "",

    "exits": {"north": "Cardiff University", "east": "City Hall", "south": "Castle"}
}

building_library = {
    "name": "Library",

    "description": "",

    "exits": {"north": "Cardiff University", "west": "Lidl", "south": "City Hall"}
}

building_lidl = {
    "name": "Lidl",

    "description": "",

    "exits": {"west": "Library"}
}

city_hall = {
    "name": "City Hall",

    "description": "",

    "exits": {"north": "Library", "east": "Student's Union", "west": "Bute Park"}
}

students_union = {
    "name": "Student's Union",

    "description": "",

    "exits": {"north": "Lidl", "east": "Mystery Location", "south": "Museum", "west": "City Hall"}
}

building_castle = {
    "name": "Castle",

    "description": "",

    "exits": {"north": "Bute Park", "east": "Museum", "west": "Mystery Location"}
}
building_museum = {
    "name": "Museum",

    "description": "",

    "exits": {"east": "Student's Unions", "south": "Shopping Centre", "west": "Castle"}
}

principality_stadium = {
    "name": "Principality Stadium",

    "description": "",

    "exits": {"north": "Castle", "east":"Museum"}
}

shopping_centre = {
    "name": "Shopping Centre",

    "description": "",

    "exits": {"north": "Museum", "south":"unknown","east": "unknown", "west":"Principality Stadium"}
}

trap_door = {
    "name": "Trap Door",

    "description": "",

    "exits": {"": ""}
}

safe_house = {
    "name": "Safe House",

    "description": "",

    "exits": {"": ""}
}

rooms = {
    "Cardiff Uni": cardiff_uni,
    "Blackweir Tavern": blackweir_tavern,
    "Bute Park": bute_park,
    "Library": building_library,
    "Lidl": building_lidl,
    "City Hall": city_hall,
    "Student's Union": students_union,
    "Castle": building_castle,
    "Museum": building_museum,
    "Principality Stadium": principality_stadium,
    "Shopping Centre": shopping_centre,
    "Mystery Location": trap_door,
    "Safe House": safe_house
}
