x_list_str = []
y_list_str = []

# Check if user input is valid

def validate_transformation(user_input, valid_transformations):

    valid_transformations = ["1", "2","translation", "reflection"]

    while user_input not in valid_transformations:
        print("\033[1mYour input is invalid. Please try again.\033[0m")
        transformation_input = input(
'''
What kind of transformation do you want to perform?
1. Translation
2. Reflection
3. W.I.P.
4. W.I.P.

'''
        ).lower()

        validate_transformation(transformation_input, valid_transformations)

        return transformation_input
        break

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
x_list_h = None
y_list_k = None 


if "translation" or "1" in transformation_input:

    # Shifts x "h" units to the left/right
    h = input("Horizontal Shift: ")
    h = eval(h)

    # Shifts y "k" units up/down
    k = input("Vertical Shift: ")
    k = eval(k)

    # Apply translation

    x_list_h = [round(x + h, 3) for x in x_list]

    y_list_k = [round(y + k, 3) for y in y_list]

# Reflection


# Make ordered pairs

og_ordered_pair =  [(x, y) for x,y in zip(x_list, y_list)]
ordered_pair =  [(x, y) for x,y in zip(x_list_h, y_list_k)]

print("Your points before the translation are:")

for i, o_o_p in enumerate(og_ordered_pair):
    print(o_o_p)

print("Your points now are:")

for i, o_p in enumerate(ordered_pair):
    print(o_p)
