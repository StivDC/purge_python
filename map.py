from items import *

cardiff_university = {

    "name": "Cardiff University",

    "description": """
    """,

    "exits": {"east": "Blackweir Tavern", "west": "Bute Park", "south": "Library"},

    "items": [item_bandage]
    
}

blackweir_tavern = {
     "name": "Blackweir Tavern",

    "description": """Its 11 o’clock. 
You hear the siren thundering around the streets as you exit the University. 
Weapons of Class Four and lower have been authorized for use during the Purge. 
All other weapons are restricted commencing at the siren.
Any and all crime, including murder will be legal for eight continuous hours for use during the Purge.
There is a safe house nearby that you know of, but there will also be people out in the streets trying to purge. 
You need to decide how you are going to survive the night. 

    """,

    "exits": {"east": "Lidl", "west": "Cardiff University"},

<<<<<<< HEAD
     "items": [item_first_aid]
=======
     "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

bute_park = {
     "name": "Bute Park",

    "description": """You enter an suspiciously quiet library.
There are books scattered everywhere and there has clearly been some conflict in here already. 
You can make out three clear exit doors.

    """,

    "exits": {"north": "Cardiff University", "east": "City Hall", "south": "Castle"},

<<<<<<< HEAD
     "items": [item_gun]
=======
     "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

building_library = {
    "name": "Library",

    "description": """You enter a dark Forest. 
The tree cover is dense and it is hard to make out the paths. 
You can hear distant noises from other things inhabiting the forest with you. 
You can see two breaks of light: one close and one far off in the distance.
    """,

    "exits": {"north": "Cardiff University", "east": "Lidl", "south": "City Hall"},

<<<<<<< HEAD
    "items": [item_key]
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

building_lidl = {
    "name": "Lidl",

    "description": """You find yourself in a half-looted shop, with its most valuable items long gone. 
You notice blood on the floor, and hope it’s not recent. 
Suddenly shelves collapse, blocking off two exits, leaving you with only one to take.
    """,

    "exits": {"west": "Library"},

<<<<<<< HEAD
    "items": [item_money]
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

city_hall = {
    "name": "City Hall",

    "description": """You walk into the main city hall. 
You think you can make out faint noises in the distance, however they do not sound welcoming. 
It is clear that you are not the first to seek refuge in this hall, 
with empty containers of food and drink scattered across the floor. 
There is only one possible exit now.
    """,

    "exits": {"north": "Library", "east": "Student's Union", "west": "Bute Park"},

    "items": [item_bandage]
}

students_union = {
    "name": "Student's Union",

    "description": """The path you take leads you to the students union.
 The floor is littered with empty bottles and food wrappers, probably from student looters.
 You can hear noises from all around however none of them seem to be close to you for the moment. 
There are three available exits.
    """,

    "exits": {"north": "Lidl", "east": "Mystery Location", "south": "Museum", "west": "City Hall"},

<<<<<<< HEAD
    "items": [item_money, item_knife]
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

building_castle = {
    "name": "Castle",

    "description": """You find yourself at the gates to the Castle. 
There are faint screams that can be heard from the other side of the castle,
 there are signs of conflict scattered around. 
There are two possible exits from the castle.
    """,

    "exits": {"north": "Bute Park", "east": "Museum", "west": "Mystery Location"},

<<<<<<< HEAD
    "items": [item_first_aid, item_gun]
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}
building_museum = {
    "name": "Museum",

    "description": """You find yourself at the gates to the Castle. 
There are faint screams that can be heard from the other side of the castle,
 there are signs of conflict scattered around. 
There are two possible exits from the castle.
    """,

    "exits": {"east": "Student's Union", "south": "Shopping Centre", "west": "Castle"},

<<<<<<< HEAD
    "items": [item_money]
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

principality_stadium = {
    "name": "Principality Stadium",

    "description": """You enter the outskirts of the principality stadium,
 and notice that there appears to be some sort of game taking place on the main pitch, 
but you’re too afraid to look. 
There is now only one available exit.
    """,

    "exits": {"north": "Castle", "east": "Museum"},

<<<<<<< HEAD
    "items": [item_knife]
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

shopping_centre = {
    "name": "Shopping Centre",

    "description": """You end up at the shopping centre, 
where most of the shops have now been looted and only a few shops are still standing.
 You can hear fighting and gun shots from some of the more expensive shops, 
scrambling for the remains. 
    """,

    "exits": {"north": "Museum", "south":"unknown","east": "unknown", "west":"Principality Stadium"},

<<<<<<< HEAD
    "items": [item_knife]
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

trap_door = {
    "name": "Trap Door",

    "description": "",

    "exits": {"": ""},

<<<<<<< HEAD
    "items": []
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
}

safe_house = {
    "name": "Safe House",

    "description": """
    ╔═══╗─────────────╔╗───╔╗───╔╗
║╔═╗║────────────╔╝╚╗──║║──╔╝╚╗
║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗
║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣
║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║
╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝
──────────╔═╝║
──────────╚══╝

You have made it to the safe house!
The purge should be over soon, but you need not worry.
You breath a sigh of relief as you slump back into your chair
and fall asleep after a restless night.
    """,

    "exits": {"": ""},

<<<<<<< HEAD
    "items": []
=======
    "items": [item_bandage]
>>>>>>> 03a29c3cb04cb113421274bcfcffb4235636cda2
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
