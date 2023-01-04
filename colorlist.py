colorlist = []
repeat = "Y"
while repeat == "Y":
    name = input("Enter a name: ")  
    colorlist.append(name)
    repeat = input("Do you want to add another name?(Y/N) ")
for i in range(len(colorlist)):
    print(i, colorlist[i])