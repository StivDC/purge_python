#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from time import sleep
import random
from events import game_events
import sys
import termcolor

#def time_left_night(i):
#    x = 8
#    y = x - i
#    if i == x:
#        return False
#    else:
#        print("There is ", y , "hours left untill the end of the purge.")

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
        print_exit(direction, exit_leads_to(exits, direction))

    #
    # COMPLETE ME!
    #

    for p_inv in inv_items:
        print("~ DROP " + p_inv["id"].upper() + " to drop " + p_inv["name"])
    
    for item in room_items:
        print("~ TAKE " + item["id"].upper() + " to take " + item["name"])
    print("\nWhat do you want to do?")

def check_if_won():
    won = True
    if current_room["name"] == "Reception":
        for i in items:
            if i in rooms["Reception"]["items"]:
                print()
            else:
                won = False
        if won == False:
            print()
        else:
            print("You've won")
    
    
def is_valid_exit(exits, chosen_exit):
  
    return chosen_exit in exits



def execute_go(direction):
    
    global current_room
    exit = is_valid_exit(current_room['exits'], direction)
    if exit:
        current_room = move(current_room['exits'], direction)
        eventID = int(random.random() * 10)
        if eventID % 2 == 1:
            print(event(eventID))
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
            check_if_won()
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

    else:
        print("This makes no sense.")

def event(eventID):
    eventID = str(eventID)
    print("\n" + str(game_events[eventID]["ascii"]) + "\n")
    print(str(game_events[eventID]["name"]) + "\n")
    print(str(game_events[eventID]["description"]) + "\n")
    
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


# This is the entry point of our programg
def main():
    i = 0
    x = 8
    print("""
████████╗██╗  ██╗███████╗    ██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗
╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██║   ██║██╔══██╗██╔════╝ ██╔════╝
   ██║   ███████║█████╗      ██████╔╝██║   ██║██████╔╝██║  ███╗█████╗  
   ██║   ██╔══██║██╔══╝      ██╔═══╝ ██║   ██║██╔══██╗██║   ██║██╔══╝  
   ██║   ██║  ██║███████╗    ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                       
""")
    print("MONEY: " + str(money) + "\nHEALTH: " + str(health) + "\n")
    cprint('Hello, World!', 'green', 'on_red')
    for x in testText:
        print(x, end='')
        sleep(uniform(0, 0.1))
    
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)
        
        # Execute the player's command
        execute_command(command)
        if x == i: 
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
            break
        elif i != x:
            i += 0.5
            y = x - i
            print("There is ", y, " Hours left in the purge!")
            

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
