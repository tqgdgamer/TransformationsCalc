import re
import math

x_list_str = []
y_list_str = []


# Validate Reflection Input

def validate_reflection(user_input, valid_input):

    patterny = r"y=([-]?(\d+|\d+\/\d+))$"
    patternx = r"x=([-]?(\d+|\d+\/\d+))$"

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

            matchy = re.match(patterny, user_input)
            matchx = re.match(patternx, user_input)

            if matchy:
                return user_input

            if matchx:
                return user_input

    return user_input

# Validate Dilation Input

def validate_dilation(user_input, valid_input):

    valid_input = ["1", "2"]

    while user_input not in valid_input:
        print("\033[1mYour input is invalid. Please try again.\033[0m")
        user_input = input(
'''
How do you want to dilate your point?
1. In respect to the origin
2. In respect to (x, y)

'''
        ).lower()

        if " " in user_input:
                user_input = user_input.replace(" ", "")

        validate_transformation(user_input, valid_input)

        return user_input
    
    return user_input

# Check if user input is valid

def validate_transformation(user_input, valid_input):

    valid_input = ["1", "2", "3", "4","translation", "reflection", "dilation", "rotation"]

    while user_input not in valid_input:
        print("\033[1mYour input is invalid. Please try again.\033[0m")
        user_input = input(
'''
What kind of transformation do you want to perform?
1. Translation
2. Reflection
3. Dilation
4. Rotation

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
3. Dilation
4. Rotation

'''
).lower()

valid_transformations = ["1", "2", "3", "4", "translation", "reflection", "dilation", "rotation"]

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
5. y = mx + b [WIP]
"""
    ).lower()

    if " " in reflection_line_input:
        reflection_line_input = reflection_line_input.replace(" ", "")

    valid_input = ["1", "2","x-axis", "y-axis"]

    reflection_line_input = validate_reflection(reflection_line_input, valid_input)

    reflection_line_input = validate_reflection(reflection_line_input, valid_input)

    matchy = re.match(r"y=([-]?(\d+|\d+\/\d+))$", reflection_line_input)
    matchx = re.match(r"x=([-]?(\d+|\d+\/\d+))$", reflection_line_input)

    if "1" in reflection_line_input or "x-axis" in reflection_line_input:
        
        X_LIST_REFLECT = [round(x, 3) for x in x_list]
        Y_LIST_REFLECT = [round(-y, 3) for y in y_list]

    if "2" in reflection_line_input or "y-axis" in reflection_line_input:
        
        X_LIST_REFLECT = [round(-x, 3) for x in x_list]
        Y_LIST_REFLECT = [round(y, 3) for y in y_list]

    if matchy:

        X_LIST_REFLECT = [round(x, 3) for x in x_list]
        Y_LIST_REFLECT = [round(-y + ( 2 * eval(matchy.group(1))), 3) for y in y_list]

    if matchx:

        X_LIST_REFLECT = [round(-x + ( 2 * eval(matchy.group(1))), 3) for x in x_list]
        Y_LIST_REFLECT = [round(y, 3) for y in x_list]

# Dilations
X_LIST_DILATE = []
Y_LIST_DILATE = []

DILATE = False

if "dilation" in transformation_input or "3" in transformation_input:

    X_LIST_DILATE = [x for x in x_list]
    Y_LIST_DILATE = [y for y in y_list]

    DILATE = True

    dilation_input = input(
"""
How do you want to dilate your point?
1. In respect to the origin
2. In respect to (x, y)

"""
    ).lower()

    valid_input = ["1", "2"]

    if "1" == dilation_input:
        scale_factor = input(
"""
What scale factor do you want to dilate your points with?\n
"""
        )

        X_LIST_DILATE = [x * eval(scale_factor) for x in x_list]
        Y_LIST_DILATE = [y * eval(scale_factor) for y in y_list]

    if "2" == dilation_input:
        
        scale_factor = input(
"""
What scale factor do you want to dilate your points with?\n
"""
        )

        respective_point = input(
"""
Where do you want to dilate your point in respect from?\n
"""
        )

        respective_point = respective_point.strip("()")
        h, k = respective_point.split(",")

        X_LIST_DILATE = [(eval(scale_factor) * (x-eval(h)) + eval(h)) for x in x_list]
        Y_LIST_DILATE = [(eval(scale_factor) * (y-eval(k)) + eval(k)) for y in y_list]

# Rotations
X_LIST_ROTATE = []
Y_LIST_ROTATE = []

ROTATE = False

if "rotation" in transformation_input or "4" in transformation_input:

    X_LIST_ROTATE = [x for x in x_list]
    Y_LIST_ROTATE = [y for y in y_list]

    ROTATE = True

    rotation_input = input(
"""
How do you want to rotate your point?
1. Clockwise
2. Counterclockwise

"""
    ).lower()

    degrees = input(
"""
How many degrees do you wish to rotate your point?
"""
    )

    degrees = eval(degrees)

    if "clockwise" in rotation_input or "1" in rotation_input:
        
        degrees = -1 * degrees
        angle = math.radians(degrees)

        X_LIST_ROTATE = [round(x*(math.cos(angle)) - y*(math.sin(angle)), 3) for x in x_list for y in y_list]
        Y_LIST_ROTATE = [round(x*(math.sin(angle)) + y*(math.cos(angle)), 3) for x in x_list for y in y_list]

    if "counterclockwise" in rotation_input or "2" in rotation_input:
    
        angle = math.radians(degrees)

        X_LIST_ROTATE = [round(x*math.cos(angle) - y*math.sin(angle), 3) for x in x_list for y in y_list]
        Y_LIST_ROTATE = [round(x*math.sin(angle) + y*math.cos(angle), 3) for x in x_list for y in y_list]



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

if DILATE is True:
    
    dilated_ordered_pair =  [(x, y) for x,y in zip(X_LIST_DILATE, Y_LIST_DILATE)]

    print("Your points now are:")

    for i, o_p in enumerate(dilated_ordered_pair):
        print(o_p)

if ROTATE is True:
    
    rotated_ordered_pair =  [(x, y) for x,y in zip(X_LIST_ROTATE, Y_LIST_ROTATE)]

    print("Your points now are:")

    for i, o_p in enumerate(rotated_ordered_pair):
        print(o_p)