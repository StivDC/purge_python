
#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from time import *
import random
from events import game_events
import sys

#Riddle idea for safe house.

py_riddles = {
    """There is a dead man in the middle of a field, 
nothing is around him and there are no footprints of any sort. 
There is an unopened package next to him.
How did he die? 
HINT: As he approached the field he knew he was going to die."
""": "Failed Parachute".lower(),

    """As I was going to the mall I met a man with seven wives,
Each wive held two bags, Each bag held a mother cat, Each mother cat had six babies,
How many people where going to the mall?
    """: "1",

    """A car's odometer shows 72927 miles, a palindromic number. 
    What are the minimum miles you would need to travel to form another? 
    (a palindrome can be read both forwards and backwards, like "Kayak")
    """: "110",

    """As a whole, I am both safe and secure. 
Behead me, and I become a place of meeting.
Behead me again, and I am the partner of ready.
Restore me, and I become the domain of beasts.
What am I?
    """: "Stable".lower(),

    """I am slim and tall, 
Many find me desirable and appealing. 
They touch me and I give a false good feeling. 
Once I shine in splendor, 
But only once and then no more. 
For many I am "to die for". 
What am I?
""": "A Cigarette".lower()
}


def list_of_items(items):
 
    item_names = ""
    for item in items:
        if item == items[-1]:

            item_names = item_names + item["name"] + ""
        else:
            item_names = item_names + item["name"] + ", "

    return item_names


def print_room_items(room):

    if len(room["items"]) != 0:
        print("There is " + list_of_items(room["items"]) + " here.")
        print()
        
def print_inventory_items(items):

    print("You have " + str(list_of_items(items) + ".\n"))
    
def print_room(room):
    
    # Display room name
    print()
    print(str(room["name"].upper()))
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
  
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):

    print("\nYou can:\n")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        if len(exits) != 0:
            print_exit(direction, exit_leads_to(exits, direction))

    for p_inv in inv_items:
        print("~ DROP " + p_inv["id"].upper() + " to drop " + p_inv["name"])
    
    for item in room_items:
        print("~ TAKE " + item["id"].upper() + " to take " + item["name"])

    for item in inv_items:
        if item["id"] == "health" or item['id'] == "bandage" or item['id'] == "firstaid":
           print("~ USE " + item["id"].upper() + " to use " + item["name"])
    print("\nWhat do you want to do?")
    
def is_valid_exit(exits, chosen_exit):
  
    return chosen_exit in exits

def check_user_ok(text):
    while True:
        print("Are you sure you want to commit this action?")
        print("Y for yes, N for no.")
        ui = input()
        if ui.upper() == "Y":
            return True
        elif ui.upper() == "N":
            return False
        else:
            print("This is an invalid input.")
            return False

def use_money(value_used):
    money -= value_used
    return money
    
def execute_use(item_id):
    global health
    global current_mass
    found = False
    for item in inventory:
        if item_id == item["id"]:
            print("")
            text = item["id"]
            if check_user_ok(text) == True:
                inventory.remove(item)
                if item_id == "health" or item_id=="bandage" or item_id=="firstaid":
                    health += 20
            elif check_user_ok() == False:
                print("You did not use your item.")
            found = True
            return
    if found == False:
        print("You cannot use that.")

def execute_go(direction):
    
    global current_room

    exit = is_valid_exit(current_room['exits'], direction)
    if exit:

        current_room = move(current_room['exits'], direction)
        eventID = int(random.random() * 10)
        if eventID % 2 == 1:
            print(event(eventID))
            event_action(eventID)
            print (eventID)
        else:
            print("SAFE MOVE")
    else:
          print("You cannot go there.")

def execute_take(item_id):

    global current_mass
    exists = 0
    room_items = current_room["items"]
    print("You took a " + str(item_id))
    if current_mass + items[item_id]['mass'] < max_mass:
        for i in range(0,len(room_items),1):
            if item_id == room_items[i]["id"]:
                inventory.append(current_room["items"][i])
                current_room["items"].pop(i)
                exists = 1
                current_mass += items[item_id]['mass']
                print("Current Mass of Inventory: " + str(current_mass))
                break
        if exists != 1:
            print("You cannot take that.")
    else:
        print("You are carrying too many items")
    
def execute_drop(item_id):
   
    global current_mass
    exists = 0
    for i in range(0,len(inventory)):
        if item_id == inventory[i]["id"]:
            current_room["items"].append(inventory[i])
            inventory.pop(i)
            exists = 1
            current_mass -= items[item_id]['mass']
            print("Current Mass of Inventory: " + str(current_mass))
            
    if exists !=1:
        print("You cannot drop that.")

def execute_command(command):

    command = command.split()
    print(command[1])

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
    else:
        print("This makes no sense.")

def event(eventID):
    eventID = str(eventID)
    print("\n" + str(game_events[eventID]["ascii"]) + "\n")
    print(str(game_events[eventID]["name"]) + "\n")
    print(str(game_events[eventID]["description"]) + "\n")

def fight_flee_bribe(text, event_name):
    player_use_item_event = False
    while player_use_item_event == False:
        if text.upper() == "F":
            for item in inventory:
                if item["id"] == "gun":
                    ui_gun = input("Do you want to use your gun? Y = Yes, N = No.")
                    if ui_gun.upper() == "Y":
                        print("You have defeated {0}, however you have lost 15 health in doing so.".format(event_name))
                        health -= 15
                        player_use_item_event = True
                        return
                    elif ui_gun.upper() == "N":
                        print("You didn't use your gun in defeating the {0} and lost 30 health.".format(event_name))
                        health -= 30
                        player_use_item_event = True
                        return
                elif item["id"] ==  "knife":
                    ui_knife = input(("Do you want to use your knife? Y = yes, N = No:"))
                    if ui_knife.upper() == "Y":
                        print("You defeat the {0}, in your attempt to flee you lose 20 health.".format(event_name))
                        health -= 20
                        player_use_item_event = True
                        return
                    elif ui_knife.upper() == "N":
                        print("You didn't use any weapons in your attempt to fight and have lost 50 health")
                        health -= 50
                        player_use_item_event = True
                        return
            print("You didn't use any weapons in your attempt to fight and have lost 50 health")
            health -= 50
            player_use_item_event = True
        elif text.upper() == "FL":
            print("You have attempted to flee and have lost a little bit of health in doing so")
            health -= 5
            player_use_item_event = True
        elif text.upper() == "B" and event_name == "Crazy_gang":
            if money >= 50:
                use_money
                player_use_item_event = True
            else:
                print("You attempted to bribe the gang but didn't have enough money and got hurt escaping")
                health -= 30
                player_use_item_event = True
        else:
            print("Invalid input")
            print("Please input either [F] to fight, [FL] to flee or [B] to Bribe.")


def check_user_ok(text):
    while True:
        print("Are you sure you want to {0} ?".format(text))
        print("Y for yes, N for no.")
        ui = input()
        if ui.upper() == "Y":
            return True
        elif ui.upper() == "N":
            return False
        else:
            print("This is an invalid input.")

def event_action(eventID):
    global health
    
    if eventID == 1:
        text = "Give Kirill your ID"
        for item in inventory:
            if item["id"] == "id":
                if check_user_ok(text) == True:
                    print("Kirill is pleased that you have your ID handy.")
                    print("He decides to give you a first aid kit in compensation.")
                    inventory.append(item_first_aid)
                    return
                elif check_user_ok(text) == False:
                    print("You decided not to show Kirill your ID")
                    print("He has left in the haste he came.")
                    break
                    return
        print("You do not have an ID and can't use Kirill's van.")
        return
    elif eventID == None:
        #fight, flee or bribe
        print("Which do you choose to do?")
        text = input(print("[F]ight, [FL]ee or [B]ribe?"))
        eventIDStr = str(eventID)
        ingame_event = game_events(eventID["id"])
        fight_flee_bribe(text, ingame_event)
    elif eventID == None:
        text = input("Do you want to [F]ight or [FL]ee?")
        eventIDStr = str(eventID)
        ingame_event = game_events(eventID["id"])
        fight_flee_bribe(text, ingame_event)
    elif eventID == 7:
        print("The sneak attack took 60 health!")
        print("Would you like to use a bandage now? It will heal you for 15 health")
        ui = False
        for item in inventory:
            if item["id"] == "bandage":
                while ui == False:
                    text = input("Y to use bandage in inventory, N to not.")
                    if text.upper() == "Y":
                        inventory.remove(item)
                        health += 15
                        return
                    elif text.upper() == "N":
                        print("Good luck!")
                        return
                    else:
                        print("Invalid input")
        print("Oh wait, you have no bandages! Best get one soon!")
    elif eventID == 9:
        
        random_item = items["knife"]["id"]
        for item in inventory:
            if random_item == item["id"]:
                print("You cannot have this item as you already have it!")
                return
        random_item_int = int(random.random() * 6)
        random_item_str = str(random_item_int)
        ui_choice = input("Do you want to pick up a knife, Y = yes, N = No.")
        ui = False
        while ui == False:
            if ui_choice.upper() == "Y":
                print("You have picked up a knife")
                inventory.append(random_item)
                ui = True
            elif ui_choice.upper() == "N":
                print("You decided to leave knife alone")
                ui = True
            else:
                print("invalid input")
    
    
def menu(exits, room_items, inv_items):

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


def move(exits, direction):
  
    return rooms[exits[direction]]
        
def print_congratulations():
     print("""
╔═══╗─────────────╔╗───╔╗───╔╗
║╔═╗║────────────╔╝╚╗──║║──╔╝╚╗
║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗
║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣
║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║
╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝
──────────╔═╝║
──────────╚══╝
You have survived the purge!
You fall flat on your back and sigh a sigh of relief.
Glad to have survived the treaded purge and live on.
                """)

# This is the entry point of our programg
def main():
    i = 0
    z = 8
    print("""
████████╗██╗  ██╗███████╗    ██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗
╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██║   ██║██╔══██╗██╔════╝ ██╔════╝
   ██║   ███████║█████╗      ██████╔╝██║   ██║██████╔╝██║  ███╗█████╗  
   ██║   ██╔══██║██╔══╝      ██╔═══╝ ██║   ██║██╔══██╗██║   ██║██╔══╝  
   ██║   ██║  ██║███████╗    ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                       
""")
    print("MONEY: " + str(money) + "\nHEALTH: " + str(health) + "\n")
    
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        random.choice(list(py_riddles.items()))
        random_riddle = int(random.random() * 5)
        for c in py_riddles:
            if c == int(random_riddle):
                print(c)
        print_room(current_room)
      
        if current_room["name"] == "Safe House":
            print_congratulations()
            sys.exit()
            return False
        else:
              print_inventory_items(inventory)
              command = menu(current_room["exits"], current_room["items"], inventory)
              execute_command(command)
        
        
        # Execute the player's command
        
        print("You have ", health, " left.")
        if health <= 0:
            print("You didn't survive the purge!")
            break

        if z == i:
            print_congratulations()
           
            break
        elif i != z:
            i += 0.5
            y = z - i
            print("There is ", y, " Hours left in the purge!")
        if current_room == "safe_house":
            random_riddle = int(random.random() * 10)
            print(py_riddles[1])

            

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
