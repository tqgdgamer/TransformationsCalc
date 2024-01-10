import re

x_list_str = []
y_list_str = []


# Check if reflection input is valid

def validate_reflection(user_input, valid_input):

    patterny = r"y=([-]?(\d+|\d+\/\d+))"
    patternx = r"x=([-]?(\d+|\d+\/\d+))"

    matchy = re.match(patterny, user_input)
    matchx = re.match(patternx, user_input)

    valid_input = ["1", "2","x-axis", "y-axis"]

    if matchy:
        return user_input

    if matchx:
        return user_input

    if not matchy and not matchx:

        while user_input not in valid_input and not matchy and not matchx:
            print("\033[1mYour input is invalid. Please try again.\033[0m")
            user_input = input(
"""
What line do you want to reflect your point over?
1. x-axis
2. y-axis
3. y = ___
4. x = ___
5. y = mx + b
"""
            ).lower()

            if " " in user_input:
                user_input = user_input.replace(" ", "")

            return user_input

    return user_input

# Check if user input is valid

def validate_transformation(user_input, valid_input):

    valid_input = ["1", "2","translation", "reflection"]

    while user_input not in valid_input:
        print("\033[1mYour input is invalid. Please try again.\033[0m")
        user_input = input(
'''
What kind of transformation do you want to perform?
1. Translation
2. Reflection
3. W.I.P.
4. W.I.P.

'''
        ).lower()

        if " " in user_input:
                user_input = user_input.replace(" ", "")

        validate_transformation(user_input, valid_input)

        return user_input
    
    return user_input


transformation_input = input(
'''
What kind of transformation do you want to perform?
1. Translation
2. Reflection
3. W.I.P.
4. W.I.P.

'''
).lower()

valid_transformations = ["1", "2","translation", "reflection"]

transformation_input = validate_transformation(transformation_input, valid_transformations)


# Amount of points

point_count = int(input("How many points do you want?\n"))

REP_POINT = 0

# Loop for how many points

while REP_POINT < point_count:

    point = input("Give a point in the format: (x, y)\n")
    point = point.strip("()")
    x, y = point.split(",")

    if ' ' in y:
        y = y.replace(' ', '')

    x_list_str.append(x)

    y_list_str.append(y)

    REP_POINT = REP_POINT + 1


# Evaluate list
x_list = [eval(i) for i in x_list_str]

y_list = [eval(i) for i in y_list_str]


# Translation
X_LIST_H = []
Y_LIST_K = []

TRANSLATE = False

if "translation" in transformation_input or "1" in transformation_input:

    TRANSLATE = True

    # Shifts x "h" units to the left/right
    h = input("Horizontal Shift: ")
    h = eval(h)

    # Shifts y "k" units up/down
    k = input("Vertical Shift: ")
    k = eval(k)

    # Apply translation

    X_LIST_H = [round(x + h, 3) for x in x_list]

    Y_LIST_K = [round(y + k, 3) for y in y_list]


# Reflection
X_LIST_REFLECT = []
Y_LIST_REFLECT = []

REFLECT = False

if "reflection" in transformation_input or "2" in transformation_input:

    patterny = r"y=([-]?(\d+|\d+\/\d+))"
    patternx = r"x=([-]?(\d+|\d+\/\d+))"

    X_LIST_REFLECT = [x for x in x_list]
    Y_LIST_REFLECT = [y for y in y_list]

    REFLECT = True
    
    reflection_line_input = input(
"""
What line do you want to reflect your point over?
1. x-axis
2. y-axis
3. y = ___
4. x = ___
5. y = mx + b
"""
    ).lower()

    if " " in reflection_line_input:
        reflection_line_input = reflection_line_input.replace(" ", "")

    valid_input = ["1", "2","x-axis", "y-axis"]

    reflection_line_input = validate_reflection(reflection_line_input, valid_input)

    reflection_line_input = validate_reflection(reflection_line_input, valid_input)

    matchy = re.match(patterny, reflection_line_input)
    matchx = re.match(patternx, reflection_line_input)

    if "1" in reflection_line_input or "x-axis" in reflection_line_input:
        
        X_LIST_REFLECT = [round(x, 3) for x in x_list]
        Y_LIST_REFLECT = [round(-y, 3) for y in y_list]

    if "2" in reflection_line_input or "y-axis" in reflection_line_input:
        
        X_LIST_REFLECT = [round(-x, 3) for x in x_list]
        Y_LIST_REFLECT = [round(y, 3) for y in y_list]

    if matchy:

        X_LIST_REFLECT = [round(x, 3) for x in x_list]
        Y_LIST_REFLECT = [round(-y + ( 2 * float(matchy.group(1))), 3) for y in y_list]

    if matchx:

        X_LIST_REFLECT = [round(-x + ( 2 * float(matchy.group(1))), 3) for x in x_list]
        Y_LIST_REFLECT = [round(y, 3) for y in x_list]

# Make ordered pairs

og_ordered_pair =  [(x, y) for x,y in zip(x_list, y_list)]

print("Your points before the transformation are:")

for i, o_o_p in enumerate(og_ordered_pair):
    print(o_o_p)

if TRANSLATE is True:

    translated_ordered_pair =  [(x, y) for x,y in zip(X_LIST_H, Y_LIST_K)]

    print("Your points now are:")

    for i, o_p in enumerate(translated_ordered_pair):
        print(o_p)

if REFLECT is True:

    reflected_ordered_pair =  [(x, y) for x,y in zip(X_LIST_REFLECT, Y_LIST_REFLECT)]

    print("Your points now are:")

    for i, o_p in enumerate(reflected_ordered_pair):
        print(o_p)