#!/usr/bin/python3

#local imports
from map import rooms
from player import *
from items import *
from gameparser import *

def list_of_items(items): # lists out a given array of items
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    output = "" #initiate empty output string
    for item in items: #iterate through the items list
        output += (", " + item['name']) #construct output
    return output[2:] # trims off the ", " from the front of the output

def print_room_items(room): # prints items in a given room
	"""This function takes a room as an input and nicely displays a list of items
	found in this room (followed by a blank line). If there are no items in
	the room, nothing is printed. See map.py for the definition of a room, and
	items.py for the definition of an item. This function uses list_of_items()
	to produce a comma-separated list of item names. For example:

	>>> print_room_items(rooms["Reception"])
	There is a pack of biscuits, a student handbook here.
	<BLANKLINE>

	>>> print_room_items(rooms["Office"])
	There is a pen here.
	<BLANKLINE>

	>>> print_room_items(rooms["Admins"])

	(no output)

	Note: <BLANKLINE> here means that doctest should expect a blank line.

	"""
	item_list = list_of_items(room['items'])
	if item_list != "":
		output = "There is "
		item_list = list_of_items(room['items'])
		output = output + item_list + " here.\n"
		print(output)
	else:
		return None

def print_inventory_items(items): # prints inventory and player information (carry weight)
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    output = "You have "
    if len(items) > 0:
        for item in items:
            output += item["name"] + ", "
        output = output[:-2] # Trims off the extra comma and spaces
    else:
        output += "no items."
    output += ".\n"
    print(output)

def print_room(room): # prints information about the room and player
	"""This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

	Note: <BLANKLINE> here means that doctest should expect a blank line.
	"""
	print("\n" + room["name"].upper() + "\n")
	print(room["description"] + "\n")
	if len(room['items']) > 0:
		print_room_items(room)

def exit_leads_to(exits, direction): # lists where a given exit leads
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to): # prints all exits from a room
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items): # function to print a menu of actions to perform
	"""This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
	print('You have a maximum carry weight of', max_carry_weight)
	print('You currently have a carry weight of', get_current_weight(inventory))
	print("You can:")
    # Iterate over available exits
	for direction in exits:
        # Print the exit name and where it leads to
		print_exit(direction, exit_leads_to(exits, direction))

	for room_item in room_items:
		print("TAKE", room_item['id'].upper(), " to take ", room_item['name'].upper(), "which weighs", room_item['weight'])

	for inv_item in inv_items:
		print("DROP", inv_item['id'].upper(), " to drop ", inv_item['name'].upper(), "which weighs", inv_item['weight'])

	print("What do you want to do?")

def is_valid_exit(exits, chosen_exit): # function to check if an exit is valid
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    bool = False # bool variable to check if exit is valid
    for exit in exits: # loops through exits
        if exit == chosen_exit: #checks if the given exit exists
            bool = True # sets the boolean value to true
    return bool # boolean value is then returned

def get_current_weight(inventory): # function to get the player's current total carry weight
    total_weight = 0 # initialise total weight variable
    for item in inventory: # loop through player's inventory
        total_weight += item['weight'] # accumulator for player's total current carry weight
    return total_weight

def is_pickup_valid(inventory, item): # checks if the player can physically pick up an item
    current_weight = get_current_weight(inventory) # gets player's current carry weight (total of items)
    if (current_weight + item['weight']) > 5:
        return False
    else:
        return True

def get_total_num_items(): # gets the total int number of items in the game world plus inventory
    total_in_inv = len(inventory) # gets the number of items in player's inventory
    total_in_rooms = 0
    for room in rooms: # loops through rooms
        for item in rooms[room]['items']: # loop for counting all items in the game world
            total_in_rooms += 1
    total_items = total_in_inv + total_in_rooms
    return total_items # returns total items in the game world plus the player's inventory

def is_game_won(): # function to see if all items are in reception (is future-proofed for more items being added)
    num_items_in_recp = 0 # number of items in reception variable initialised
    for items in rooms['Reception']['items']: # loops through the items in reception
        num_items_in_recp += 1 # adds to count of items in reception
    total_items = get_total_num_items()
    if total_items == num_items_in_recp: # check victory conditions
        return True
    else:
        return False

def execute_go(direction): # executes a go command to change rooms
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room # sets the current room variable to a global so it can be changed in this function
    exits = current_room['exits']
    if is_valid_exit(exits, direction):
        current_room = rooms[current_room['exits'][direction]]
    else:
        print("You cannot go there.")

def execute_take(item_id): # executes a take command to pick up an item
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    success = False
    for items in current_room['items']: # loop through room's items
        if items['id'] == item_id:
            if is_pickup_valid(inventory, items) == True: # check if an item can be physically picked up
                current_room['items'].remove(items) # removes item from current room item pool
                inventory.append(items) # adds item to inventory
                print(item_id, " added to inventory") # print message showing success
                success = True
    if success == False:
        print("You cannot take that")

def execute_drop(item_id): # executes an item drop to drop an item
	"""This function takes an item_id as an argument and moves this item from the
	player's inventory to list of items in the current room. However, if there is
	no such item in the inventory, this function prints "You cannot drop that."
	"""
	
	success = False
	for items in inventory: # loops through inventory
		if item_id == items['id']:
			current_room['items'].append(items) # adds item to room's item pool
			inventory.remove(items) # removes item from inventory
			print(items['name'], "dropped") # success message
			success = True
	if success == False:
		print("You cannot drop that")

def execute_command(command): # command sorting function
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

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


def menu(exits, room_items, inv_items): # function to print out all informationt to player
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


def move(exits, direction): # gets the next room to move to
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]



# This is the entry point of our program
def main(): #main game loop
    won = False # initalise win condition bool
    # Main game loop

    #check game victory status
    while won == False:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        #check if game is won
        won = is_game_won()

        # if game is won, print victory message
        if won == True:
            print("========================")
            print("Congratulations!")
            print("You have won the game")
            print("========================")

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
