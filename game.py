"""
Do not remove this file. Ensure your main function is in this file.

I will execute your game like this:

python3 game.py

Yes, you may add additional files to this folder.
"""
import random
import time
import math
import itertools


EXP = (100, 300, 700)
ROOMS = ("\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n",
         "\033[0;35mArcade Room\033[0m. The room is huge but all the machines are broken. You can see the wires\n"
         "hanging down from the ceiling.\n",
         "\033[0;35mBoxing Room\033[0m. The heavy bags are all worn out! Someone must have used them frequently..\n",
         "\033[0;35mKitchen\033[0m. The appliances are covered in dust and spider web but there are some pizza boxes\n"
         "on the counter. The pizzas look eatable!\n",
         "\033[0;35mTheatre\033[0m. They even have an opera theatre! The only light source is from the stage\n"
         "spotlight.\n",
         "\033[0;35mMelisa's Bedroom\033[0m. There is a picture frame facing down on the night stand. You walk over\n"
         "and pick it up. It's a picture of Melisa with her family. You feel really sorry for her.\n",
         "\033[0;35mDinning Room\033[0m. A couple of candles on the table light up the area. You can see some\n"
         "left-over pizza slices on the plate. Someone must have been here!\n",
         "\033[0;35mGuest Room\033[0m. This room looks like another abandoned basement! Of course, you wonder who\n"
         "would visit this place..\n",
         "\033[0;35mWine Cellar\033[0m. The room is filled with wine bottles and barrels! You are tempted to open a\n"
         "bottle and take a sip, but you realize you have to focus on getting out of here!\n",
         "\033[0;35mExhibition Room\033[0m. You look around and almost fell on your knees when you see the shelves\n"
         "are filled with jars containing brains that are floating in the liquid!!\n",
         "\033[0;35mLuke's Toy Room\033[0m. This could be Melisa's son room. You saw him in the picture in Melisa's\n"
         "bedroom. You hope the boy made it out alive with his dad. The train toy suddenly runs which startles you..\n",
         "\033[0;35mRed Room\033[0m. This room looks familiar. Did you see it somewhere else? Maybe in a movie?\n",
         "\033[0;35mCar Garage\033[0m. There is only one old, rusty car here. Why would they build such a huge car\n"
         "garage on an island you wonder..\n",
         "\033[0;35mAbandoned Lab\033[0m. You see several flasks filled with liquid on the table. You wonder what\n"
         "they are working on..\n",
         "\033[0;35mWorkshop\033[0m. Looks like it's a wood workshop because saws are seen everywhere. You take one\n"
         "step closer to the table saw and almost squeal like a little girl because you see blood still dripping from\n"
         "the saw blade!\n",
         "\033[0;35mLibrary\033[0m. This library is huge! You find yourself lost in a maze of bookshelves.\n",
         "\033[0;35mDarwin's Office\033[0m. This room looks like a disaster. The intruders must have flipped this\n"
         "place upside down to look for the research.\n",
         "\033[0;35mSauna\033[0m. The charcoal was long put out. This room is nothing but darkness0.\n",
         "\033[0;35mWorship Room\033[0m. You have never seen that many reliquaries in your life!\n")
DIRECTIONS = {"1": "NORTH", "2": "EAST", "3": "SOUTH", "4": "WEST", "5": 'Quit'}
CLASSES = {"1": 'MMA Fighter', "2": 'Olympic Archer', "3": 'Unemployed Magician', "4": 'Elite Fencer'}
CLASS_A_STARTING_POINT = {'class_name': CLASSES["1"], 'level_name': ('Featherweight', 'Lightweight', 'Heavyweight'),
                          'skill': ('Lightning Jabs', 'Destructive Roundhouse', 'Deontay Punches'), 'HP': 500,
                          'max_HP': 500, 'damage': 120, 'stamina': 100, 'accuracy': 80}
CLASS_B_STARTING_POINT = {'class_name': CLASSES["2"], 'level_name': ('Kindergarten', 'High school', 'Master'),
                          'skill': ('Flying Flip-flop', 'Shooting Butter Knives', 'Poisonous Arrows'), 'HP': 500,
                          'max_HP': 500, 'damage': 80, 'stamina': 100, 'accuracy': 120}
CLASS_C_STARTING_POINT = {'class_name': CLASSES["3"], 'level_name': ('Mage', 'Wizard', 'Sakura CardCaptor'),
                          'skill': ('Spiky Roses', 'Bunny Spirit Summon', 'Cursed Playing Cards'), 'HP': 600,
                          'max_HP': 600, 'damage': 100, 'stamina': 80, 'accuracy': 100}
CLASS_D_STARTING_POINT = {'class_name': CLASSES["4"], 'level_name': ('Rookie', 'Local Fencer', 'International Fencer'),
                          'skill': ('Clothes Hanger Strike', 'Ranging Sweeper', 'Sabre Slash'), 'HP': 400,
                          'max_HP': 400, 'damage': 100, 'stamina': 120, 'accuracy': 100}
LEVEL1_FOE_NAMES = ('Part-time Thief', 'Gatekeeper', 'Mutated Hamster')
LEVEL2_FOE_NAMES = ('Full-time Thief', 'Chihuahua', 'High school Gangster')
LEVEL3_FOE_NAMES = ('Majestic Mainecoon', 'Insane Researcher', 'Boss Secretary')
LV1_FOE = {'name': ('Part-time Thief', 'Gatekeeper', 'Mutated Hamster'), 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
LV2_FOE = {'name': ('Full-time Thief', 'Chihuahua', 'High school Gangster'), 'foe_HP': 300, 'foe_damage': 100,
           'foe_exp': 70}
LV3_FOE = {'name': ('Majestic Mainecoon', 'Insane Researcher', 'Boss Secretary'), 'foe_HP': 400, 'foe_damage': 150,
           'foe_exp': 100}
BOSS = {'name': 'PSYCHO', 'x-coor': 7, 'y-coor': 7, 'foe_HP': 2000, 'foe_damage': 200}
VICTORY_MESSAGE = """\n\033[1;30;42m\t\t\t\t\t\t\t\t\tCONGRATULATION ON YOUR VICTORY!!\t\t\t\t\t\t\t\t\t\033[0m\n
\033[1;32m
_______                                   ____      ________         ____                          ____
|  ____|                                __|  |__   |___  ___|        |  |                          |  |
|  |__   ___   __  ___    ___     ___  |__    __|     |  |     ___   |  |     ___ __  __  ___    __|  |
|   __| / _ \  | \/  _|  / _ \   / _ \    |  |        |  |    /  __\ |  |    / _   | |   _   \  / _   |
|  |   | |_| | |   /    | |_| | | |_| |   |  |      __|  |__  _\  \  |  |__ | |_|  | |  | |  | | |_|  |
|__|    \___/  |__|      \__  |  \___/    |_ |     |________| |____/  \___/  \___/_| |__| |__|  \ ____|
                         __|  |
                         \____|
\033[0m"""


def animate_message(message: str):
    """
    Display the message using ANSI escape for styling and time.sleep for animation effect

    :param message: a string representing the message to be printed
    :precondition: message must be a string
    :postcondition: successfully print the message with the desired effect
    """
    list_of_letters = map(str.upper, message)
    for letter in list_of_letters:
        print("\033[1;31m" + letter + "\033[0m", end=" ")
        time.sleep(0.5)


def make_board(row: int, column: int) -> dict:
    """
    Return a dictionary containing the pairs of location and location description

    :param row: an integer larger than or equal to 10 representing the number of rows
    :param column: an integer larger than or equal to 10 representing the number of columns
    :precondition: row must be an integer
    :precondition: column must be an integer
    :postcondition: successfully create a board containing locations and location description based on the arguments
    :return: a dictionary containing the pairs of location and location description
    """
    board = {(row_coordinate, column_coordinate): ROOMS[random.randint(0, len(ROOMS) - 1)]
             for row_coordinate in range(row) for column_coordinate in range(column)}
    return board


def character_setup():
    """
    Return a dictionary containing the character information at starting point

    :postcondition: correctly create a character based on the user input
    :return: a dictionary containing the character information
    """
    print("\033[1;30;42m[\t\t\t\t\t\t\t\t\tCreate a new character to play the game\t\t\t\t\t\t\t\t\t]\033[0m\n")
    return {'name': input('Enter character name: '), 'level': 1, 'exp': EXP[0], 'x-coor': 0,
            'y-coor': 0, 'class': class_assignment()}


def class_assignment():
    """
    Return a dictionary containing the information of the class chosen by the user at starting point

    :postcondition: correctly assign the class based on the user input
    :return: a dictionary containing the information of the class
    """
    for num, class_choice in enumerate(CLASSES.values(), 1):
        print(num, class_choice)
    user_choice = 0
    while user_choice not in CLASSES:
        user_choice = input("Please enter the number representing your class choice: ")
    if user_choice == "1":
        return CLASS_A_STARTING_POINT.copy()
    elif user_choice == "2":
        return CLASS_B_STARTING_POINT.copy()
    elif user_choice == "3":
        return CLASS_C_STARTING_POINT.copy()
    else:
        return CLASS_D_STARTING_POINT.copy()


def game_intro(character: dict):
    """
    Display the game introduction on the screen

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary containing the character information
    :postcondition: correctly print the game introduction and welcoming message including character name
    """
    name = character['name']
    print("\n\n\033[1;30;42m[\t\t\t\t\t\t\t\t\t\t\tWelcome to Forgot Island\t\t\t\t\t\t\t\t\t\t]\033[0m"
          "\n\nGame intro:"
          "\n\nYou wake up, finding yourself lying on a dusty wooden floor of something that looks like an abandoned "
          "\nbasement. Suddenly there is a voice coming from behind..")
    time.sleep(3)
    print(f"\nMelisa: Thanks God. You've woke up, {name}. You have lost consciousness for 2 days!")
    time.sleep(3)
    print("\nRight! You start to remember.."
          "\n\nYou were on your way to your friend's party when someone struck you from behind. Everything blacked out "
          "\nimmediately. Now you find yourself in a strange place. Who did that to you? And who is this pale woman, "
          "\nisn't she too pale for an alive person?")
    time.sleep(3)
    print("\nMelisa: You're right. I'm no longer alive.. That's why I can read your mind. You were kidnapped by PSYCHO,"
          "\nthe invader of this place. I and my husband were working on a research of human genetic intervention when"
          "\nPSYCHO took over our mansion and caused my death. He stole half of our research! Fortunately, my husband,"
          "\nDarwin, was able to escape with the other half. For years, PSYCHO has kidnapped several people and "
          "\ncarried out the experiment on them. "
          "\n\nThe only way to escape is to take him down. Please take back the research from him and find my husband "
          f"\nat: 1000 Autumn Place. Take care, {name}!\n")
    print("\033[1;30;42m[\t\t\t\t\t\t\t\t\t\t\t\t\tGAME START\t\t\t\t\t\t\t\t\t\t\t\t]\033[0m\n")


def get_direction(board: dict, character: dict) -> str:
    """
    Return the direction chosen by the user

    :param board: a dictionary containing the pairs of location and location description
    :param character: a dictionary containing the character information
    :precondition: board must be a dictionary
    :precondition: character must be a dictionary
    :postcondition: correctly return the direction chosen by the user
    :return: a string representing the direction
    """
    print("\nYour current location is: ({0}, {1})".format(character['x-coor'], character['y-coor']))
    print("Your current \033[1;32mHP\033[0m: ({0}/{1})\n".format(character['class']['HP'],
                                                                 character['class']['max_HP']))
    ascii_map(board, character)
    print()
    for num, direction in zip(itertools.count(1), DIRECTIONS.values()):
        print(num, direction)
    user_direction = 0
    while user_direction not in DIRECTIONS:
        user_direction = input("\nEnter the number representing the direction: ")
    return DIRECTIONS[user_direction]


def ascii_map(board: dict, character: dict):
    """
    Display a map telling the current location of the character

    :param board: a dictionary containing the pairs of location and location description
    :param character: a dictionary containing the character information
    :precondition: board must be a dictionary
    :precondition: character must be a dictionary
    :postcondition: the map correctly shows the current location of the character
    """
    guide_map = {key: '[ ]' for key in board}
    coordinate_list = list(board)
    size = int(math.sqrt(len(board)))
    grouped_coordinate_list = [coordinate_list[index:index + size] for index in range(0, len(coordinate_list), size)]
    for coordinate in guide_map:
        if coordinate == (character['x-coor'], character['y-coor']):
            guide_map[coordinate] = '[x]'
    count = 0
    while count < size:
        for column in grouped_coordinate_list:
            print(guide_map[column[count]], end=' ')
        count += 1
        print()


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Return True if the move chosen by the user is valid, otherwise return False

    :param board: a dictionary containing the pairs of location and location description
    :param character: a dictionary containing the character information
    :param direction: a string representing the direction
    :precondition: board must be a dictionary
    :precondition: character must be a dictionary
    :precondition: direction must be a string
    :postcondition: correctly determine if the character in allowed to move in chosen direction
    :return: True if the move is valid, otherwise return False

    >>> char = {'x-coor': 0, 'y-coor': 0}
    >>> grid = make_board(3, 3)
    >>> validate_move(grid, char, 'NORTH')
    False
    >>> char = {'x-coor': 2, 'y-coor': 2}
    >>> grid = make_board(3, 3)
    >>> validate_move(grid, char, 'NORTH')
    True
    """
    if direction == 'NORTH':
        new_location = (character['x-coor'], character['y-coor'] - 1)
    elif direction == 'EAST':
        new_location = (character['x-coor'] + 1, character['y-coor'])
    elif direction == 'SOUTH':
        new_location = (character['x-coor'], character['y-coor'] + 1)
    else:
        new_location = (character['x-coor'] - 1, character['y-coor'])
    return new_location in board


def encounter_boss(character: dict) -> bool:
    """
    Return True if the character reaches a location where the boss is assigned

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :postcondition: correctly determine if the character encounters the boss
    :return: True if the character encounters the boss, otherwise return False

    >>> char = {'x-coor': 2, 'y-coor': 2}
    >>> encounter_boss(char)
    False
    >>> char = {'x-coor': 7, 'y-coor': 7}
    >>> encounter_boss(char)
    True
    """
    return character['x-coor'] == BOSS['x-coor'] and character['y-coor'] == BOSS['y-coor']


def boss_alive(boss: dict) -> bool:
    """
    Return True if the boss hit point is larger than 0, otherwise return False

    :param boss: a dictionary containing the boss information
    :precondition: boss must be a dictionary
    :postcondition: correctly determine if the boss is still alive
    :return: True if the boss hit point is larger than 0, otherwise return False

    >>> boss_test = {'foe_HP': -5}
    >>> boss_alive(boss_test)
    False
    >>> boss_test = {'foe_HP': 150}
    >>> boss_alive(boss_test)
    True
    >>> boss_test = {'foe_HP': 0}
    >>> boss_alive(boss_test)
    False
    """
    return boss['foe_HP'] > 0


def foe_alive(foe: dict) -> bool:
    """
    Return True if the foe hit point is larger than 0, otherwise return False

    :param foe: a dictionary containing the foe information
    :precondition: foe must be a dictionary
    :postcondition: correctly determine if the foe is still alive
    :return: True if the foe hit point is larger than 0, otherwise return False

    >>> foe_test = {'foe_HP': -1}
    >>> foe_alive(foe_test)
    False
    >>> foe_test = {'foe_HP': 1}
    >>> foe_alive(foe_test)
    True
    >>> foe_test = {'foe_HP': 0}
    >>> foe_alive(foe_test)
    False
    """
    return foe['foe_HP'] > 0


def update_position(board: dict, character: dict, direction: str):
    """
    Print the description of the character current location

    :param board: a dictionary containing the pairs of location and location description
    :param character: a dictionary containing the character information
    :param direction: a string representing the direction
    :precondition: board must be a dictionary
    :precondition: character must be a dictionary
    :precondition: direction must be a string
    :postcondition: correctly display the description of character current location
    """
    if direction == 'NORTH':
        character['y-coor'] -= 1
    elif direction == 'EAST':
        character['x-coor'] += 1
    elif direction == 'SOUTH':
        character['y-coor'] += 1
    else:
        character['x-coor'] -= 1
    print("\nYou've entered the", board[(character['x-coor'], character['y-coor'])])


def user_choice_to_fight():
    """
    Return True if user choose to fight, otherwise return False

    :postcondition: correctly return the choice of the user
    :return: True if user choose to fight, otherwise return False
    """
    user_choice = ''
    while user_choice.lower() != 'y' and user_choice.lower() != 'n':
        user_choice = input("You want to fight the enemy or not? y/n: ")
    return user_choice == 'y'


def twenty_percent_chance():
    """
    Return True or False randomly with 20% chance for True and 80% chance for False

    :postcondition: correctly return the random choice based on the ratio
    :return: True or False randomly with 20% chance for True and 80% chance for False
    """
    return random.choices([True, False], weights=[1, 4], k=1).pop()


def foe_type(character: dict) -> dict:
    """
    Return a foe that is suitable to the character level

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :postcondition: correctly return a foe based on the character level
    :return: a dictionary containing the foe information

    >>> char = {'level': 1}
    >>> foe_type(char)
    {'name': ('Part-time Thief', 'Gatekeeper', 'Mutated Hamster'), 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
    >>> char = {'level': 2}
    >>> foe_type(char)
    {'name': ('Full-time Thief', 'Chihuahua', 'High school Gangster'), 'foe_HP': 300, 'foe_damage': 100, 'foe_exp': 70}
    """
    if character['level'] == 1:
        return LV1_FOE.copy()
    elif character['level'] == 2:
        return LV2_FOE.copy()
    else:
        return LV3_FOE.copy()


def character_attack(character: dict) -> bool:
    """
    Return True if the character successfully makes any damage to the enemy, otherwise return False

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :postcondition: randomly return True or False, the probability is based on the character class
    :return: True if the character successfully makes any damage to the enemy, otherwise return False
    """
    if character['class']['class_name'] == CLASSES['1']:
        return random.choices([True, False], weights=[70, 30], k=1).pop()
    elif character['class']['class_name'] == CLASSES['2']:
        return random.choices([True, False], weights=[90, 10], k=1).pop()
    else:
        return random.choices([True, False], weights=[80, 20], k=1).pop()


def foe_attack(foe: dict) -> bool:
    """
    Return True if the foe successfully makes any damage to the character, otherwise return False

    :param foe: a dictionary containing the foe information
    :precondition: foe must be a dictionary
    :postcondition: randomly return True or False, the probability is based on the foe level
    :return: True if the foe successfully makes any damage to the character, otherwise return False
    """
    if foe['name'] in LEVEL1_FOE_NAMES:
        return random.choices([True, False], weights=[70, 30], k=1).pop()
    elif foe['name'] in LEVEL2_FOE_NAMES:
        return random.choices([True, False], weights=[60, 40], k=1).pop()
    else:
        return random.choices([True, False], weights=[50, 50], k=1).pop()


def attack_while_fleeing(character: dict, foe: dict):
    """
    Adjust the character hit point if the character is attacked during fleeing and print the update message

    :param character: a dictionary containing the character information
    :param foe: a dictionary containing the foe information
    :precondition: character must be a dictionary
    :precondition: foe must be a dictionary
    :postcondition: correctly adjust the character hit point
    """
    attacked_while_fleeing = twenty_percent_chance()
    if attacked_while_fleeing:
        character['class']['HP'] -= random.randint(30, foe['foe_damage'])
        print('Ouch! You were attacked while fleeing! Your HP is now {0}'.format(character['class']['HP']))
    else:
        print("Successfully escaped!")


def battle_round(character: dict, foe: dict):
    """
    Adjust the character or foe hit point when one making damage to the other and print corresponding messages

    :param character: a dictionary containing the character information
    :param foe: a dictionary containing the foe information
    :precondition: character must be a dictionary
    :precondition: foe must be a dictionary
    :postcondition: correctly deduct the hit point of whom receiving the damage and print corresponding messages
    """
    if character_attack(character):
        foe['foe_HP'] -= random.randint(50, character['class']['damage'])
        print('You successfully struck your enemy!!')
    else:
        print('You missed!')
    if foe_attack(foe):
        character['class']['HP'] -= random.randint(30, foe['foe_damage'])
        print('Ouch! Your enemy fired back! Your hit point is now {0}'.format(character['class']['HP']))


def battle_foe(character: dict, foe: dict):
    """
    Battle between the foe and the character

    :param character: a dictionary containing the character information
    :param foe: a dictionary containing the foe information
    :precondition: character must be a dictionary
    :precondition: foe must be a dictionary
    :postcondition: end the battle based on the while loop and correctly print the corresponding message
    """
    user_fight, foe_flee = True, False
    while foe_alive(foe) and user_fight and not foe_flee:
        battle_round(character, foe)
        if character['class']['HP'] <= 50:
            print("Your HP is too low. Escape attempt..")
            user_fight = False
        foe_flee = twenty_percent_chance()
        time.sleep(2)
    if not foe_flee and not user_fight:
        attack_while_fleeing(character, foe)
    elif not foe_alive(foe):
        character['exp'] += foe['foe_exp']
        print("You have destroyed your enemy with {0}! You've collected {1}exp!".format(
            character['class']['skill'][character['level'] - 1], foe['foe_exp']))
    else:
        print("Your opponent has fled the scene!")


def battle_boss(character: dict, boss: dict):
    """
    Battle between the boss and the character

    :param character: a dictionary containing the character information
    :param boss: a dictionary containing the boss information
    :precondition: character must be a dictionary
    :precondition: boss must be a dictionary
    :postcondition: end the battle based on the while loop and correctly print the corresponding message
    """
    user_fight = True
    while boss_alive(boss) and user_fight:
        battle_round(character, boss)
        if character['class']['HP'] <= 50:
            print("Your HP is too low. Escape attempt..")
            user_fight = False
        time.sleep(2)
    if not user_fight:
        attack_while_fleeing(character, boss)
    else:
        print("Unbelievable!! {0} is down!!!".format(boss['name']))


def heal(character: dict):
    """
    Increase the character hit point if the current hit point is lower than the maximum hit point

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :postcondition: correctly Increase the character hit point if the current hit point is lower than the maximum
                    hit point
    """
    if character['class']['HP'] < character['class']['max_HP']:
        character['class']['HP'] += 50
    if character['class']['HP'] > character['class']['max_HP']:
        character['class']['HP'] = character['class']['max_HP']


def events(character: dict, boss: dict):
    """
    The event that may happen when the character makes a move

    :param character: a dictionary containing the character information
    :param boss: a dictionary containing the boss information
    :precondition: character must be a dictionary
    :precondition: boss must be a dictionary
    :postcondition: correctly execute the event based on the user input
    """
    encounter_foe = twenty_percent_chance()
    if encounter_boss(character):
        print("You have encountered the boss!!")
        if user_choice_to_fight():
            battle_boss(character, boss)
        else:
            attack_while_fleeing(character, boss)
    elif encounter_foe:
        foe = foe_type(character)
        foe_name = foe['name'][random.randint(0, len(foe['name']) - 1)]
        print("You are blocked by a {0}".format(foe_name))
        if user_choice_to_fight():
            battle_foe(character, foe)
        else:
            attack_while_fleeing(character, foe)
    else:
        heal(character)
        print("There's nothing here. Keep moving!")


def character_alive(character: dict) -> bool:
    """
    Return True if the character is alive, otherwise return False

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :postcondition: correctly determine if the character is still alive based on the hit point
    :return: True if the character hit point is larger than 0, otherwise return False

    >>> char = {'class': {'HP': 1}}
    >>> character_alive(char)
    True
    >>> char = {'class': {'HP': 0}}
    >>> character_alive(char)
    False
    """
    return character['class']['HP'] > 0


def level_up_check(character: dict) -> bool:
    """
    Return True if the character has leveled up, otherwise return False

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :postcondition: correctly determine if the character has leveled up based on the current level and experience
    :return: True if the character has leveled up, otherwise return False

    >>> char = {'exp': 299, 'level': 1}
    >>> level_up_check(char)
    False
    >>> char = {'exp': 301, 'level': 1}
    >>> level_up_check(char)
    True
    >>> char = {'exp': 301, 'level': 2}
    >>> level_up_check(char)
    False
    >>> char = {'exp': 800, 'level': 2}
    >>> level_up_check(char)
    True
    """
    return character['exp'] >= EXP[character['level']]


def level_up(character: dict):
    """
    Adjust the character stats to reflect the level up event

    :param character: a dictionary containing the character information
    :precondition: character must be a dictionary
    :postcondition: correctly adjust the character information and print out the new stats
    """
    if character['level'] < 3 and level_up_check(character):
        character['level'] += 1
        character['class']['max_HP'] += character['level'] * 300
        character['class']['HP'] = character['class']['max_HP']
        character['class']['damage'] += 75
        character['class']['stamina'] += 50
        character['class']['accuracy'] += 50
        print("You've levelled up, {0}! Here's your current stats: \n"
              "Level: {1}\n"
              "Class name: {2}\n"
              "Skills: {3}\n"
              "HP: {4}\n"
              "Damage: {5}\n"
              "Stamina: {6}\n"
              "Accuracy: {7}".format(character['name'], character['level'],
                                     character['class']['level_name'][character['level'] - 1],
                                     character['class']['skill'][character['level'] - 1],
                                     character['class']['HP'], character['class']['damage'],
                                     character['class']['stamina'], character['class']['accuracy']))


def game():
    """
    Start executing the game
    """
    char = character_setup()
    game_intro(char)
    board = make_board(10, 10)
    boss = BOSS.copy()
    direction = True
    while boss_alive(boss) and direction and character_alive(char):
        direction = get_direction(board, char)
        if direction == 'Quit':
            direction = False
        elif validate_move(board, char, direction):
            update_position(board, char, direction)
            events(char, boss)
            level_up(char)
        else:
            print("Inaccessible")
    if not direction:
        print("\n\033[1;31mYou've quit.\033[0m")
    elif not character_alive(char):
        print("\n\033[1;31mYou died.\033[0m\n")
        animate_message("Game Over")
    else:
        print(VICTORY_MESSAGE)


def main():
    game()


if __name__ == "__main__":
    main()
