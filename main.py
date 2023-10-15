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

# Shifts x "h" units to the left/right
h = int(input("Horizontal Shift: "))

# Shifts y "k" units up/down
k = int(input("Vertical Shift: "))

# Convert str to int
# Apply translation

x_list = [eval(i) for i in x_list_str]
x_list_h = [x + h for x in x_list]

y_list = [eval(i) for i in y_list_str]
y_list_k = [y + k for y in y_list]

# Make ordered pairs

og_ordered_pair =  [(x, y) for x,y in zip(x_list, y_list)]
ordered_pair =  [(x, y) for x,y in zip(x_list_h, y_list_k)]

print("Your points before the translation are:")

for i in range(len(og_ordered_pair)):
    print(og_ordered_pair[i])

print("Your points now are:")

for i in range(len(ordered_pair)):
    print(ordered_pair[i])
