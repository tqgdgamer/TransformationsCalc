from ast import literal_eval

x_list_str = []
y_list_str = []

point_count = int(input("How many points do you want?\n"))

rep_point = 0

# Loop for how many points

while rep_point < point_count:

    point = input("Give a point in the format: (x, y)\n")
    point = point.strip("()")
    x, y = point.split(",")

    x_list_str.append(x)

    y_list_str.append(y)

    rep_point = rep_point + 1

# Evaluate list
x_list = [literal_eval(i) for i in x_list_str]

y_list = [literal_eval(i) for i in y_list_str]

# Shifts x "h" units to the left/right
h = input("Horizontal Shift: ")
h = literal_eval(h)

# Shifts y "k" units up/down
k = input("Vertical Shift: ")
k = literal_eval(k)

# Apply translation

x_list_h = [round(x + h, 3) for x in x_list]

y_list_k = [round(y + k, 3) for y in y_list]

# Make ordered pairs

og_ordered_pair =  [(x, y) for x,y in zip(x_list, y_list)]
ordered_pair =  [(x, y) for x,y in zip(x_list_h, y_list_k)]

print("Your points before the translation are:")

for i in range(len(og_ordered_pair)):
    print(og_ordered_pair[i])

print("Your points now are:")

for i in range(len(ordered_pair)):
    print(ordered_pair[i])
