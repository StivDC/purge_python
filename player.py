from items import *
from map import rooms

global health
global money

inventory = [item_id, item_laptop, item_money]

health = 100
money = 0

# Start game at the reception
current_room = rooms["Blackweir Tavern"]
