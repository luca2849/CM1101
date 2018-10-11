#!/usr/bin/python3
from map import rooms
import string
import re


def remove_punct(text):
    text = re.sub(r'[^\w\s]','',text)
    return text
    
def remove_spaces(text):
    text = text.replace(" ", "")
    return text


def normalise_input(user_input):
    user_input_normalised = remove_punct(remove_spaces(user_input)).lower()
    return user_input_normalised
    
def display_room(room):
	print("\n", room["name"].upper(), "\n")
	print(room["description"], "\n")
    
def exit_leads_to(exits, direction):
    if exits[direction] != "":
        print(exits[direction])

def print_menu_line(direction, leads_to):
    print("Go ", direction.upper(), "to ", leads_to)

def print_menu(exits):
    print("You can:")
    for exit in exits:
        print_menu_line(exit, exits[exit])
    print("Where do you want to go?")

def is_valid_exit(exits, user_input):
    bool = False
    for exit in exits:
        if exit == user_input:
            bool = True
    return bool

def menu(exits):
    # Repeat until the player enter a valid choice
    for exit in exits: 
        # Display menu
        print_menu(exits)
        # Read player's input
        choice = input()
        # Normalise the input
        choice_normalised = normalise_input(choice)
        # Check if the input makes sense (is valid exit)
        if is_valid_exit(exits, choice_normalised) == True:
            return choice_normalised
        else:
            print("Invalid Direction, Please Try Again")


def move(exits, direction):
    new_current_room = exits[direction]
    return rooms[new_current_room]


# This is the entry point of our program
def main():
    # Start game at the reception
    current_room = rooms["Reception"]

    # Main game loop
    while True:
        # Display game status (room description etc.)
        display_room(current_room)
        # What are the possible exits from the current room?
        exits = current_room["exits"]
        # Show the menu with exits and ask the player
        direction = menu(exits)
        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
