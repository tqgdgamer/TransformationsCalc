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
        y_reflect = eval(matchy.group(1))
        return y_reflect
    
    if matchx:
        x_reflect = eval(matchx.group(1))
        return x_reflect

    if not matchy and not matchx:

        while user_input not in valid_input:
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

            validate_reflection(user_input, valid_input)

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

        validate_transformation(user_input, valid_input)

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

validate_transformation(transformation_input, valid_transformations)

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
X_LIST_H = None
Y_LIST_K = None
TRANSLATE = False
REFLECT = False

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

if "reflection" in transformation_input or "2" in transformation_input:

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

    reflection_line = validate_reflection(reflection_line_input, valid_input)

    print(reflection_line)

# Make ordered pairs

og_ordered_pair =  [(x, y) for x,y in zip(x_list, y_list)]

print("Your points before the translation are:")

for i, o_o_p in enumerate(og_ordered_pair):
    print(o_o_p)

if TRANSLATE is True:

    translated_ordered_pair =  [(x, y) for x,y in zip(X_LIST_H, Y_LIST_K)]

    print("Your points now are:")

    for i, o_p in enumerate(translated_ordered_pair):
        print(o_p)

if REFLECT is True:

    print("Your points now are:")

    print("Work In Progress")
