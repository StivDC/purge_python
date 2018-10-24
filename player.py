from items import *
from map import rooms

global health
global money

inventory = [item_id, item_knife, item_money]

health = 100
money = 0
current_mass = 0
max_mass = 7
status = "Alive"

#Start game at the Blackweir Tavern
current_room = rooms["Blackweir Tavern"]
