from items import *

cardiff_university = {

    "name": "Cardiff University",

    "description": "",

    "exits": {"east": "Blackweir Tavern", "west": "Bute Park", "south": "Library"},

    "items": [item_pen]
    
}

blackweir_tavern = {
     "name": "Blackweir Tavern",

    "description": "",

    "exits": {"east": "Lidl", "west": "Cardiff University"},

     "items": [item_pen]
}

bute_park = {
     "name": "Bute Park",

    "description": "",

    "exits": {"north": "Cardiff University", "east": "City Hall", "south": "Castle"},

     "items": [item_pen]
}

building_library = {
    "name": "Library",

    "description": "",

    "exits": {"north": "Cardiff University", "west": "Lidl", "south": "City Hall"},

    "items": [item_pen]
}

building_lidl = {
    "name": "Lidl",

    "description": "",

    "exits": {"west": "Library"},

    "items": [item_pen]
}

city_hall = {
    "name": "City Hall",

    "description": "",

    "exits": {"north": "Library", "east": "Student's Union", "west": "Bute Park"},

    "items": [item_pen]
}

students_union = {
    "name": "Student's Union",

    "description": "",

    "exits": {"north": "Lidl", "east": "Mystery Location", "south": "Museum", "west": "City Hall"},

    "items": [item_pen]
}

building_castle = {
    "name": "Castle",

    "description": "",

    "exits": {"north": "Bute Park", "east": "Museum", "west": "Mystery Location"},

    "items": [item_pen]
}
building_museum = {
    "name": "Museum",

    "description": "",

    "exits": {"east": "Student's Union", "south": "Shopping Centre", "west": "Castle"},

    "items": [item_pen]
}

principality_stadium = {
    "name": "Principality Stadium",

    "description": "",

    "exits": {"north": "Castle", "east":"Museum"},

    "items": [item_pen]
}

shopping_centre = {
    "name": "Shopping Centre",

    "description": "",

    "exits": {"north": "Museum", "south":"unknown","east": "unknown", "west":"Principality Stadium"},

    "items": [item_pen]
}

trap_door = {
    "name": "Trap Door",

    "description": "",

    "exits": {"": ""},

    "items": [item_pen]
}

safe_house = {
    "name": "Safe House",

    "description": "",

    "exits": {"": ""},

    "items": [item_pen]
}

rooms = {
    "Cardiff University": cardiff_university,
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
