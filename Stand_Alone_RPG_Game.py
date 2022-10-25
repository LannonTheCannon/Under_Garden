# Simply RPG Game
import random
###

# Parts (Cities)
# 1. DSI Display Connector............DSI Display Hall 
# 2. GPIO Input/Output Header.........GPIO Input/Output Electric Plant 
# 3. Wireless Bluetooth...............Wireless Bluetooth Bank
# 4. Micro SD Card Slot...............Micro SD Card Park
# 5. 2-Lane MIPI DSI Display Port.....
# 6. USB-C Power Port 5V..............USB-C Power Plant 
# 7. Micro HDMI ports.................HDMI Display Hall
# 8. 2-Lane MIPI Camera Port..........Camera Studio Facility
# 9. 4-Pole Stereo Audio..............Stereo Audio Sound Center
# 10. USB 3.0 Port....................USB 3.0 Information Hub
# 11. Gigabit Ethernet................Gigabit Ethernet Freeway

# Enter the mind of the A.I. and try to find its virus.
# Destroy the virus and bring peace and prosperity to the
# AI Infrastructure.

def showInstructions():
    # print a main menu and the commands

    print('''

RPG Game
++++++++

    Get to the Garden with a key and a potion
    Avoid the monsters!

    Commands:
    go [direction]
    get [item]

''')

def showStatus():
    # print the player's current status
    print('-----------------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('---------------')

# an inventory, which is empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall': {
            'down' : 'Kitchen',
            'right' : 'Dining Room',
            'item' : 'key'
            },
    'Kitchen' : {
            'up' : 'Hall',
            'item' : 'monster',
            'right' : 'Living Room'
            },
    'Dining Room' : {
            'left' : 'Hall',
            'right': 'Garage',
            'south' : 'Garden',
            'item' : 'potion'
            },

    'Living Room' : {
            'up' : 'Dining Room',
            'right' : 'Garden',
            'left' : 'Kitchen',
            'down':'Pool Area'
            },

    'Pool Area' : {
            'up' : 'Living Room',
            'left' : 'Upstairs',
            'right' : 'Backyard'
            },
    'Garden' : {
            'up' : 'Dining Room',
            'left' : 'Living Room',
            'down' : 'Backyard'
            },
    'Garage' : {
            'left' : 'Dining Room',
            'down' : 'Garden'
            },
    'Backyard' : {
            'up' : 'Garden',
            'left' : 'Pool Area'
            },
    'Upstairs' : {
            'upstairs' : 'Hallway',
            'item' : 'enchilada'
            },
    'Hallway' : {
            'up' : 'Bathroom',
            'right' : 'Study',
            },
    'Study' : {
            'up' : 'Game Room',
            'left' : 'Hallway',
            'right' : 'Balcony',
            'item' : 'fishing rod'
            },
    'Balcony' : {
            'up' : 'Washroom',
            'left' : 'Study',
            'item' : 'notebook'
            },
    'Washroom' : {
            'up' : 'Master Bedroom',
            'left' : 'Game Room',
            'down' : 'Balcony'
            },
    'Game Room' : {
            'up': 'Bedroom 2',
            'down' : 'Study', 
            'left' : 'Bathroom',
            'right' : 'Washroom',
            },
    'Bathroom' : {
            'up' : 'Bedroom 1',
            'right' : 'Game Room',
            'down': 'Hallway'
            },

    'Bedroom 1' : {
            'right' : 'Bedroom 2',
            'down' : 'Bathroom'
            },

    'Bedroom 2' : {
            'left' : 'Bedroom 1',
            'right' : 'Master Bedroom',
            'down' : 'Game Room'
            },

    'Master Bedroom' : {
            'left' : 'Bedroom 2',
            'down' : 'Washroom',
            'item' : 'evidence'
            },
    
}

# Start the player in the hall
currentRoom = 'Hall'


showInstructions()

# loop forever
while True:

    showStatus()

    # Get the player next 'move'
    # .split() breaks it up into a list array
    # e.g. typing 'go east' would give the list:
    # ['go','east']

    # Input Validation 
    move = ''
    while move == '':
        move = input('> ')

    # Once it's good lets split up each word using NLP 
    move = move.lower().split()

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are alowed wherever the ywantt o go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            #monsterRoom = rooms[]
            # add monster move
            print(random.choice(list(rooms)))
            ####################

        else:
            print('You can\'t go that way!')

            

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one hey want to get
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']

        else:
            # tell them tehy can't get it
            print('Can\'t get '+ move[1] + '!')

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you...Game Over')
        break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... You WIN!')
        break






            
























