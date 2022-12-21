colors = []

num_colors = int(input("How many colors would you like to add? "))

while len(colors) < num_colors:
    color = input("Enter a color: ")
    colors.append(color)

for color in colors:
    print(color)

