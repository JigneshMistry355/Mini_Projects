import random   

dice_art = {
    1:(
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2:(
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3:(
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4:(
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5:(
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6:(
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    )
}

DIE_HEIGHT = len(dice_art[1])
DIE_WIDTH = len(dice_art[1][0])
DIE_FACE_SEPARATOR = " "

# this function will convert 'number_of_dice_input' into integer
def parse_input(input_string):
    numbers = {'1','2','3','4','5','6'}
    # the strip function will remove whitespaces in input (from beginning or at the end)
    if input_string.strip() in numbers:
        return int(input_string)
    else:
        print("please enter numbers between 1-6")
        raise SystemExit(1)
    
def roll_dice(number_of_dice):
    roll_results = []
    for i in range(number_of_dice):
        roll = random.randint(1,6)
        roll_results.append(roll)
    return roll_results

def generate_dice_faces_diagram(dice_values):
    # this list contains a list of all rows of single dice diagram, separated like [(dice diagram elements),(dice...),(dice...)].
    dice_faces = []
    #dice values contains values from roll_results list
    for values in dice_values:
        dice_faces.append(dice_art[values])
    # print(dice_faces)

    dice_faces_rows = []
    # This loop will run for 5[0-4] times... len(DIE_HEIGHT = 5)
    for row in range(DIE_HEIGHT):
        row_components = []
        # die corresponds to all the rows of a single dice diagram, ie [(---die1---),(---die2---)]
        for die in dice_faces:
            # die[row] calls each index of each die at a time.
            # 1st index element of die1, die2,...die n,  at a time, then second index element, and so on.
            row_components.append(die[row])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    # return dice_faces_rows

    # width is the length equal to size of index 0 of dice_faces_rows list 
    Width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(Width, "~")
    dice_faces_diagram = "\n".join([diagram_header]+dice_faces_rows)
    return dice_faces_diagram


    
# ~~~~~~~~~~~~~~Driver code~~~~~~~~~~~~~~~~~
# take input for number of dice
# input in python is always stored as string
number_of_dice_input = input("How many dice do you want to roll [1-6]")
number_of_dice = parse_input(number_of_dice_input)
# print(type(number_of_dice))
roll_value = roll_dice(number_of_dice)
# print(roll_value)
print(generate_dice_faces_diagram(roll_value))