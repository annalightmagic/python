colorlist = ['red', 'blue', 'yellow', 'green', 'purple', 'white']
print("You can print one color, index numbers go from 0 to", len(colorlist) - 1)
i = int(input("Which color do you want to print?: "))
while i >= len(colorlist):
    i = int(input("Enter correct number please: "))
print(colorlist[i])